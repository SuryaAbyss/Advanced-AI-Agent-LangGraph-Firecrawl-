from typing import Dict, Any
from langgraph.graph import StateGraph, END
from openai import OpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from .models import CompanyAnalysis, CompanyInfo, ResearchState
from .firecrawl import FirecrawlService
from .prompts import DeveloperToolsPrompts


class Workflow:
    def __init__(self):
        self.firecrawl = FirecrawlService()
        # Initialize OpenAI client with OpenRouter for DeepSeek
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
        )
        # Create a custom LLM wrapper for DeepSeek
        self.llm = self._create_deepseek_llm()
        self.prompts = DeveloperToolsPrompts()
        self.workflow = self._build_workflow()

    def _create_deepseek_llm(self):
        """Create a custom LLM wrapper for DeepSeek through OpenRouter"""
        class DeepSeekLLM:
            def __init__(self, client, temperature=0.1):
                self.client = client
                self.temperature = temperature
            
            def invoke(self, messages):
                # Convert langchain messages to OpenAI format
                openai_messages = []
                for msg in messages:
                    if isinstance(msg, SystemMessage):
                        openai_messages.append({"role": "system", "content": msg.content})
                    elif isinstance(msg, HumanMessage):
                        openai_messages.append({"role": "user", "content": msg.content})
                
                response = self.client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": "https://github.com/your-repo",  # Optional
                        "X-Title": "AI Agent",  # Optional
                    },
                    model="deepseek/deepseek-chat-v3-0324:free",
                    messages=openai_messages,
                    temperature=self.temperature
                )
                
                # Return a response object that mimics langchain response
                class MockResponse:
                    def __init__(self, content):
                        self.content = content
                
                return MockResponse(response.choices[0].message.content)
            
            def with_structured_output(self, output_class):
                """Return self for compatibility with structured output calls"""
                return self
        
        return DeepSeekLLM(self.client, temperature=0.1)

    def _build_workflow(self):
        graph = StateGraph(ResearchState)
        graph.add_node("extract_tools", self._extract_tools)
        graph.add_node("research", self._get_company_info)
        graph.add_node("analyze", self._analyze_step)
        graph.set_entry_point("extract_tools")
        graph.add_edge("extract_tools", "research")
        graph.add_edge("research", "analyze")
        graph.add_edge("analyze", END)
        return graph.compile()

    def _extract_tools(self, state: ResearchState) -> Dict[str, Any]:
        print(f"Finding Articles about : {state.query}")

        #goes and searches for articles about the query lookup the urls
        articles_query = f"{state.query} tools comparision best alternatives"
        search_results = self.firecrawl.search_companies(articles_query, num_results = 5)

        #scrape the content of the articles
        all_content = ""
        
        # Handle SearchResponse object
        if hasattr(search_results, 'data'):
            results_to_process = search_results.data
        else:
            results_to_process = search_results
            
        for result in results_to_process:
            # Handle both tuple and dictionary formats
            if isinstance(result, tuple):
                # If result is a tuple, assume first element is URL
                url = result[0] if len(result) > 0 else ""
            else:
                # If result is a dictionary, use get method
                url = result.get("url", "")
            
            scraped = self.firecrawl.scrape_company_pages(url)
            if scraped and hasattr(scraped, 'markdown'):
                all_content += scraped.markdown[:1500] + "\n\n"

        messages = [
            SystemMessage(content=self.prompts.TOOL_EXTRACTION_SYSTEM),
            HumanMessage(content=self.prompts.tool_extraction_user(state.query, all_content))
        ]
           #extract the tools from the articles
        try:
            response = self.llm.invoke(messages)
            tool_names = [
                name.strip()
                for name in response.content.strip().split("\n")
                if name.strip()
            ]
            print(f"Extracted Tools: {','.join(tool_names[:5])}")
            return {"extracted_tools": tool_names}
        except Exception as e:
            print(e)
            return {"extracted_tools": []}
        
    def _analyze_company_content(self, company_name: str, content: str) -> CompanyAnalysis:
        messages = [
            SystemMessage(content=self.prompts.TOOL_ANALYSIS_SYSTEM),
            HumanMessage(content=self.prompts.tool_analysis_user(company_name, content))
        ]
         
        try:
            response = self.llm.invoke(messages)
            # For now, return a basic analysis since structured output is complex
            # You might want to implement JSON parsing here
            return CompanyAnalysis(
                pricing_model="Unknown",
                is_open_source=False,
                tech_stack=[],
                description=response.content[:500] if response.content else "",
                api_available=False,
                language_support=[],
                integration_capabilities=[]
            )
        except Exception as e:
            print(e)
            return CompanyAnalysis(
                pricing_model="Unknown",
                is_open_source=False,
                tech_stack=[],
                description="",
                api_available=False,
                language_support=[],
                integration_capabilities=[]
            )
        #this is the function which is used to get the company info
    
    def _get_company_info(self, state: ResearchState) -> Dict[str, Any]:
        extracted_tools = getattr(state, "extracted_tools", [])

        #if no tools are extracted, then we will search for the tools directly
        if not extracted_tools:
            print("No tools extracted found, falling back to direct search")
            search_results = self.firecrawl.search_companies(state.query, num_results=5)
            # Handle SearchResponse object
            if hasattr(search_results, 'data'):
                results_to_process = search_results.data
            else:
                results_to_process = search_results
                
            tool_names = []
            for result in results_to_process:
                if result:
                    if isinstance(result, tuple):
                        # If result is a tuple, try to extract title from it
                        if len(result) > 1 and hasattr(result[1], 'get'):
                            tool_names.append(result[1].get("title", "Unknown"))
                        else:
                            tool_names.append("Unknown")
                    else:
                        # If result is a dictionary, use get method
                        tool_names.append(result.get("metadata", {}).get("title", "Unknown"))
        else:
            tool_names = extracted_tools[:4]

        print(f"Searching specific tools: {','.join(tool_names[:5])}")

        companies = []
        for tool_name in tool_names:
            tool_search_results = self.firecrawl.search_companies(tool_name + "official site" , num_results=1)
             
            #if the tool is found, then we will scrape the company page
            if tool_search_results:
                # Handle SearchResponse object
                if hasattr(tool_search_results, 'data') and tool_search_results.data:
                    result = tool_search_results.data[0]
                elif isinstance(tool_search_results, list) and tool_search_results:
                    result = tool_search_results[0]
                else:
                    continue
                
                # Handle both tuple and dictionary formats
                if isinstance(result, tuple):
                    url = result[0] if len(result) > 0 else ""
                    description = result[1].get("markdown", "") if len(result) > 1 and hasattr(result[1], 'get') else ""
                else:
                    url = result.get("url", "")
                    description = result.get("markdown", "")

                #create a company info object
                company = CompanyInfo(
                    name = tool_name,
                    description=description,
                    website=url,
                    tech_stack=[],
                    competitors=[]
                )
                
                #scrape the company page
                scraped = self.firecrawl.scrape_company_pages(url)
                if scraped and hasattr(scraped, 'markdown'):
                    content = scraped.markdown
                    analysis = self._analyze_company_content(company.name, content)

                  
                    company.pricing_model = analysis.pricing_model
                    company.is_open_source = analysis.is_open_source
                    company.tech_stack = analysis.tech_stack
                    company.description = analysis.description
                    company.api_available = analysis.api_available
                    company.language_support = analysis.language_support
                    company.integration_capabilities = analysis.integration_capabilities

                    companies.append(company)

        return {"companies": companies}
    
    def _analyze_step(self, state: ResearchState) -> Dict[str, Any]:
        print("Generating recommendation")

        company_data = ", ".join([
            company.model_dump_json() for company in state.companies
        ])

        messages = [
            SystemMessage(content=self.prompts.RECOMMENDATION_SYSTEM),
            HumanMessage(content=self.prompts.recommendation_user(state.query, company_data))
        ]

        response = self.llm.invoke(messages)
        return {"analysis": response.content}
    
    def run(self, query: str) -> ResearchState:
        initial_state = ResearchState(query=query)
        final_state = self.workflow.invoke(initial_state)
        return ResearchState(**final_state)