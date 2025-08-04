from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio
import os

load_dotenv() 

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # More efficient, higher free tier limits
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY"),
    max_retries=3,
    request_timeout=60
)

server_params = StdioServerParameters(
    command = "npx",
    env ={
        "FIRECRAWLER_API_KEY": os.getenv("FIRECRAWL_API_KEY")
    },
    args = ["firecrawl-mcp"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model, tools)

            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can scrape websites, crawl pages, and extract data using Firecrawl tools. Think step by step and use the appropriate tools to help the user."
                }
            ]

            print("Available tools -", *[tool.name for tool in tools])
            print("-" * 60)

            while True:
                user_input = input("\nYou: ")
                if user_input == "quit":
                    print("Exiting...")
                    break

                messages.append({"role": "user", "content": user_input[:175000]})

                try:
                    agent_response = agent.invoke({"messages": messages})

                    ai_message = agent_response["messages"][-1].content
                    print("\nAgent:", ai_message)
                except Exception as e:
                    print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())








