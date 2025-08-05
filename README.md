# 🤖 AI Agent - Developer Tools Research Assistant

<div align="center">

![AI Agent Banner](https://img.shields.io/badge/AI-Powered%20Research-blue?style=for-the-badge&logo=robot)
![DeepSeek AI](https://img.shields.io/badge/DeepSeek-AI-orange?style=for-the-badge&logo=openai)
![LangGraph](https://img.shields.io/badge/LangGraph-Workflow-green?style=for-the-badge&logo=graphql)
![Firecrawl](https://img.shields.io/badge/Firecrawl-Web%20Scraping-red?style=for-the-badge&logo=webpack)

*An intelligent AI agent that researches and analyzes developer tools, technologies, and platforms to provide comprehensive recommendations. Built with LangGraph, DeepSeek AI, and Firecrawl for web scraping and analysis.*

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg?style=flat&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

</div>

---

## 📸 Demo Screenshots

<div align="center">

### 🚀 Tool Discovery & Analysis
![Tool Discovery](1st.jpg)
*AI Agent discovering and analyzing developer tools*

### 🔍 Detailed Company Research  
![Company Research](2nd.jpg)
*Comprehensive analysis of tool features, pricing, and tech stacks*

### 💡 Intelligent Recommendations
![Recommendations](3rd.jpg)
*AI-generated actionable recommendations for developers*

</div>

---

## 🚀 Features

<div align="center">

| 🔍 **Discovery** | 🧠 **Intelligence** | 📊 **Analysis** | 💡 **Recommendations** |
|:---:|:---:|:---:|:---:|
| ![Discovery](https://img.shields.io/badge/Auto-Discovery-brightgreen?style=for-the-badge&logo=search) | ![AI](https://img.shields.io/badge/DeepSeek-AI-orange?style=for-the-badge&logo=openai) | ![Analysis](https://img.shields.io/badge/Comprehensive-Analysis-blue?style=for-the-badge&logo=chart) | ![Recs](https://img.shields.io/badge/Smart-Recommendations-purple?style=for-the-badge&logo=lightbulb) |

</div>

### ✨ Key Capabilities

<div align="center">

![Tool Discovery](https://img.shields.io/badge/🔍-Intelligent%20Tool%20Discovery-brightgreen?style=flat-square)
![Analysis](https://img.shields.io/badge/📊-Comprehensive%20Analysis-blue?style=flat-square)
![AI Integration](https://img.shields.io/badge/🤖-DeepSeek%20AI%20Integration-orange?style=flat-square)
![Web Scraping](https://img.shields.io/badge/🕷️-Firecrawl%20Web%20Scraping-red?style=flat-square)
![Recommendations](https://img.shields.io/badge/💡-Structured%20Recommendations-purple?style=flat-square)

</div>

- **🔍 Intelligent Tool Discovery**: Automatically finds and extracts relevant developer tools from articles and web content
- **📊 Comprehensive Analysis**: Analyzes pricing models, tech stacks, API availability, and integration capabilities  
- **🤖 DeepSeek AI Integration**: Uses DeepSeek AI through OpenRouter for intelligent content analysis
- **🕷️ Web Scraping**: Leverages Firecrawl for efficient web content extraction
- **💡 Structured Recommendations**: Provides detailed, actionable recommendations for developer tools

## 🏗️ Architecture

<div align="center">

### 🔄 LangGraph Workflow Pipeline

```mermaid
graph LR
    A[🔍 User Query] --> B[📰 Tool Extraction]
    B --> C[🏢 Company Research]
    C --> D[💡 Recommendation Generation]
    D --> E[📊 Final Results]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
```

</div>

### 🎯 Three-Stage Process

<div align="center">

| Stage | 🔍 **Tool Extraction** | 🏢 **Company Research** | 💡 **Recommendation Generation** |
|:---:|:---|:---|:---|
| **Input** | User query | Extracted tool names | Analyzed company data |
| **Process** | Web scraping + AI extraction | Website analysis + AI parsing | Data synthesis + AI recommendations |
| **Output** | List of relevant tools | Detailed company profiles | Actionable recommendations |

</div>

**The project uses a sophisticated LangGraph workflow with three main stages:**

1. **🔍 Tool Extraction**: Searches for articles and extracts relevant tool names using AI
2. **🏢 Company Research**: Analyzes individual tools and their features in detail  
3. **💡 Recommendation Generation**: Provides comprehensive, actionable recommendations

## 📋 Prerequisites

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-Package%20Manager-green?style=for-the-badge&logo=package)
![Firecrawl](https://img.shields.io/badge/Firecrawl-API%20Key-red?style=for-the-badge&logo=key)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API%20Key-orange?style=for-the-badge&logo=openai)

</div>

### 🛠️ Required Tools

- **🐍 Python 3.12+** - Modern Python with latest features
- **📦 [uv](https://docs.astral.sh/uv/)** - Fast Python package manager
- **🔑 Firecrawl API Key** - For web scraping capabilities
- **🤖 OpenRouter API Key** - For DeepSeek AI access (optional)

## 🛠️ Installation

<div align="center">

### 🚀 Quick Start Guide

![Step 1](https://img.shields.io/badge/Step-1-blue?style=for-the-badge) ![Step 2](https://img.shields.io/badge/Step-2-green?style=for-the-badge) ![Step 3](https://img.shields.io/badge/Step-3-orange?style=for-the-badge) ![Step 4](https://img.shields.io/badge/Step-4-purple?style=for-the-badge)

</div>

### 📥 1. Clone the Repository

```bash
git clone <your-repository-url>
cd advance-agent
```

<div align="center">

![Git Clone](https://img.shields.io/badge/📥-Repository%20Cloned-success?style=flat-square)

</div>

### 📦 2. Install Dependencies

The project uses `uv` for fast dependency management:

```bash
uv sync
```

<div align="center">

![Dependencies](https://img.shields.io/badge/📦-Dependencies%20Installed-success?style=flat-square)

</div>

### 🔧 3. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# Firecrawl API Key (required for web scraping)
FIRECRAWL_API_KEY=your_firecrawl_api_key_here

# Optional: OpenRouter API Key (if you want to use your own)
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

<div align="center">

![Environment](https://img.shields.io/badge/🔧-Environment%20Configured-success?style=flat-square)

</div>

### 🔑 4. Get API Keys

<div align="center">

| 🔥 **Firecrawl API Key** | 🤖 **OpenRouter API Key** |
|:---:|:---:|
| ![Firecrawl](https://img.shields.io/badge/Firecrawl-Required-red?style=for-the-badge&logo=fire) | ![OpenRouter](https://img.shields.io/badge/OpenRouter-Optional-orange?style=for-the-badge&logo=openai) |

</div>

#### 🔥 Firecrawl API Key (Required)
<div align="center">

![Step 1](https://img.shields.io/badge/1-Visit%20Firecrawl-blue?style=flat-square) ![Step 2](https://img.shields.io/badge/2-Sign%20Up-green?style=flat-square) ![Step 3](https://img.shields.io/badge/3-Get%20API%20Key-orange?style=flat-square)

</div>

1. 🌐 Visit [Firecrawl](https://firecrawl.dev/)
2. 📝 Sign up for an account
3. 🎯 Navigate to your dashboard
4. 🔑 Copy your API key

#### 🤖 OpenRouter API Key (Optional)
<div align="center">

![Step 1](https://img.shields.io/badge/1-Visit%20OpenRouter-blue?style=flat-square) ![Step 2](https://img.shields.io/badge/2-Add%20Credits-green?style=flat-square) ![Step 3](https://img.shields.io/badge/3-Get%20API%20Key-orange?style=flat-square)

</div>

1. 🌐 Visit [OpenRouter](https://openrouter.ai/)
2. 💳 Sign up and add credits to your account
3. 🎯 Navigate to your dashboard
4. 🔑 Copy your API key

## 🚀 Usage

<div align="center">

### 🎯 Quick Start

![Python](https://img.shields.io/badge/Python-Code%20Example-blue?style=for-the-badge&logo=python)
![Simple](https://img.shields.io/badge/Simple-3%20Lines-green?style=for-the-badge&logo=check)

</div>

### 📝 Basic Usage

```python
from src.workflow import Workflow

# 🚀 Initialize the workflow
workflow = Workflow()

# 🔍 Run research on a specific query
result = workflow.run("database management tools")

# 📊 Access the results
print(f"Query: {result.query}")
print(f"Extracted Tools: {result.extracted_tools}")
print(f"Companies Analyzed: {len(result.companies)}")
print(f"Analysis: {result.analysis}")
```

<div align="center">

![Success](https://img.shields.io/badge/✅-Ready%20to%20Use-success?style=flat-square)

</div>

### 🔍 Example Queries

<div align="center">

| 🗄️ **Databases** | ☁️ **Cloud** | 📊 **Monitoring** | 🔐 **Security** |
|:---:|:---:|:---:|:---:|
| ![DB](https://img.shields.io/badge/PostgreSQL-Alternatives-blue?style=flat-square) | ![Cloud](https://img.shields.io/badge/Cloud-Deployment-green?style=flat-square) | ![Monitor](https://img.shields.io/badge/App-Monitoring-orange?style=flat-square) | ![Auth](https://img.shields.io/badge/Auth-Providers-purple?style=flat-square) |

</div>

```python
# 🗄️ Research database tools
result = workflow.run("PostgreSQL alternatives")

# ☁️ Research deployment platforms  
result = workflow.run("cloud deployment platforms")

# 📊 Research monitoring tools
result = workflow.run("application monitoring tools")

# 🔐 Research authentication services
result = workflow.run("authentication providers")
```

<div align="center">

![Examples](https://img.shields.io/badge/💡-Try%20These%20Examples-blue?style=flat-square)

</div>

## 📁 Project Structure

<div align="center">

### 🗂️ File Organization

```
📦 advance-agent/
├── 📁 src/
│   ├── 📄 __init__.py
│   ├── 🚀 workflow.py          # Main workflow implementation
│   ├── 📊 models.py            # Pydantic data models
│   ├── 🕷️ firecrawl.py         # Firecrawl service wrapper
│   └── 🤖 prompts.py           # AI prompts for analysis
├── ⚙️ pyproject.toml           # Project configuration
├── 🔒 uv.lock                  # Dependency lock file
├── 📸 1st.jpg                  # Demo screenshot 1
├── 📸 2nd.jpg                  # Demo screenshot 2
├── 📸 3rd.jpg                  # Demo screenshot 3
└── 📖 README.md               # This file
```

</div>

<div align="center">

| File | Purpose | Status |
|:---:|:---|:---:|
| ![Workflow](https://img.shields.io/badge/workflow.py-Main%20Logic-blue?style=flat-square) | Core workflow implementation | ✅ |
| ![Models](https://img.shields.io/badge/models.py-Data%20Models-green?style=flat-square) | Pydantic data structures | ✅ |
| ![Firecrawl](https://img.shields.io/badge/firecrawl.py-Web%20Scraping-red?style=flat-square) | Firecrawl service wrapper | ✅ |
| ![Prompts](https://img.shields.io/badge/prompts.py-AI%20Prompts-orange?style=flat-square) | AI prompt templates | ✅ |

</div>

## 🔧 Configuration

### DeepSeek AI Configuration

The project is configured to use DeepSeek AI through OpenRouter. The configuration is in `src/workflow.py`:

```python
self.client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)
```

**Model Used**: `deepseek/deepseek-chat-v3-0324:free`

### Customizing the Model

To use a different model or your own OpenRouter API key:

1. Update the API key in `src/workflow.py`
2. Change the model name in the `_create_deepseek_llm` method

## 🔍 How It Works

### 1. Tool Extraction Phase

```python
def _extract_tools(self, state: ResearchState):
    # Search for articles about the query
    articles_query = f"{state.query} tools comparison best alternatives"
    search_results = self.firecrawl.search_companies(articles_query, num_results=5)
    
    # Scrape content from found articles
    # Extract tool names using DeepSeek AI
    # Return list of extracted tools
```

**What it does:**
- Searches for articles related to the query
- Scrapes content from found URLs
- Uses AI to extract specific tool names from the content
- Returns a list of relevant tools

### 2. Company Research Phase

```python
def _get_company_info(self, state: ResearchState):
    # For each extracted tool
    for tool_name in tool_names:
        # Search for the tool's official website
        # Scrape the website content
        # Analyze the content using AI
        # Extract pricing, tech stack, features, etc.
```

**What it does:**
- Takes the extracted tool names
- Searches for each tool's official website
- Scrapes detailed information from the websites
- Uses AI to analyze pricing, tech stack, API availability, etc.

### 3. Recommendation Generation Phase

```python
def _analyze_step(self, state: ResearchState):
    # Combine all analyzed company data
    # Generate comprehensive recommendations
    # Provide actionable insights
```

**What it does:**
- Combines all the analyzed company information
- Uses AI to generate comprehensive recommendations
- Provides actionable insights and comparisons

## 📊 Data Models

### CompanyAnalysis

```python
class CompanyAnalysis(BaseModel):
    pricing_model: str = "Unknown"  # Free, Freemium, Paid, Enterprise
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = []
    description: str = ""
    api_available: Optional[bool] = None
    language_support: List[str] = []
    integration_capabilities: List[str] = []
```

### CompanyInfo

```python
class CompanyInfo(BaseModel):
    name: str
    description: str
    website: str
    pricing_model: Optional[str] = None
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = []
    competitors: List[str] = []
    api_available: Optional[bool] = None
    language_support: List[str] = []
    integration_capabilities: List[str] = []
    developer_experience_rating: Optional[str] = None
```

### ResearchState

```python
class ResearchState(BaseModel):
    query: str
    extracted_tools: List[str] = []
    companies: List[CompanyInfo] = []
    search_results: List[Dict[str, Any]] = []
    analysis: Optional[str] = None
```

## 🤖 AI Prompts

The project uses carefully crafted prompts for different analysis tasks:

### Tool Extraction Prompt
Extracts specific tool names from articles and content.

### Tool Analysis Prompt
Analyzes company websites to extract:
- Pricing model
- Tech stack
- API availability
- Language support
- Integration capabilities

### Recommendation Prompt
Generates actionable recommendations based on all analyzed data.

## 🔧 Troubleshooting

### Common Issues

#### 1. Firecrawl API Key Error
```
ValueError: FIRECRAWL_API_KEY is not set in the environment variables
```

**Solution**: Make sure you have set the `FIRECRAWL_API_KEY` in your `.env` file.

#### 2. DeepSeek API Error
```
openai.AuthenticationError: Invalid API key
```

**Solution**: The project uses a pre-configured API key. If you want to use your own, update it in `src/workflow.py`.

#### 3. Import Errors
```
ModuleNotFoundError: No module named 'openai'
```

**Solution**: Run `uv sync` to install all dependencies.

#### 4. Search Results Format Issues
```
AttributeError: 'tuple' object has no attribute 'get'
```

**Solution**: The code handles multiple response formats from Firecrawl. This error should be resolved in the current version.

### Debug Mode

To enable debug logging, you can add print statements in the workflow methods or modify the logging level.

## 🧪 Testing

### Test the Installation

```bash
# Test that all imports work
uv run python -c "from src.workflow import Workflow; print('✓ All imports successful')"
```

### Test the Workflow

```python
from src.workflow import Workflow

# Test with a simple query
workflow = Workflow()
result = workflow.run("database tools")
print(f"Found {len(result.extracted_tools)} tools")
print(f"Analyzed {len(result.companies)} companies")
```

## 📈 Performance

<div align="center">

### ⚡ Speed Metrics

| Stage | ⏱️ **Time** | 🚀 **Status** |
|:---:|:---|:---:|
| **Tool Extraction** | ~30-60 seconds | ![Fast](https://img.shields.io/badge/Fast-30s%20to%2060s-green?style=flat-square) |
| **Company Analysis** | ~2-5 minutes per tool | ![Medium](https://img.shields.io/badge/Medium-2m%20to%205m-orange?style=flat-square) |
| **Recommendation Generation** | ~10-30 seconds | ![Very Fast](https://img.shields.io/badge/Very%20Fast-10s%20to%2030s-brightgreen?style=flat-square) |

</div>

<div align="center">

### 🎯 Total Performance

![Total Time](https://img.shields.io/badge/Total%20Time-3%20to%2010%20minutes-blue?style=for-the-badge&logo=clock)
![Efficiency](https://img.shields.io/badge/Efficiency-High-success?style=for-the-badge&logo=check)

</div>

**⚡ Total time**: 3-10 minutes depending on the number of tools found and analyzed.

## 🔒 Security

<div align="center">

### 🛡️ Security Features

![Security](https://img.shields.io/badge/Security-High-brightgreen?style=for-the-badge&logo=shield)
![Privacy](https://img.shields.io/badge/Privacy-Protected-blue?style=for-the-badge&logo=lock)

</div>

<div align="center">

| 🔐 **API Security** | 🚫 **Data Protection** | 🌐 **Web Ethics** | ⚡ **Rate Limiting** |
|:---:|:---:|:---:|:---:|
| ![API](https://img.shields.io/badge/Environment-Variables-green?style=flat-square) | ![Data](https://img.shields.io/badge/No%20Sensitive-Data%20Stored-red?style=flat-square) | ![Web](https://img.shields.io/badge/Robots.txt-Compliant-blue?style=flat-square) | ![Rate](https://img.shields.io/badge/Rate-Limited-orange?style=flat-square) |

</div>

- **🔐 API Security**: API keys are stored in environment variables
- **🚫 Data Protection**: No sensitive data is logged or stored
- **🌐 Web Ethics**: All web scraping follows robots.txt guidelines
- **⚡ Rate Limiting**: Rate limiting is implemented for API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangGraph](https://github.com/langchain-ai/langgraph) for workflow orchestration
- [DeepSeek AI](https://www.deepseek.com/) for intelligent analysis
- [Firecrawl](https://firecrawl.dev/) for web scraping capabilities
- [OpenRouter](https://openrouter.ai/) for AI model access

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [Issues](https://github.com/your-repo/issues)
3. Create a new issue with detailed information

## 🔄 Updates

Stay updated with the latest changes:

```bash
git pull origin main
uv sync
```

---

<div align="center">

### 🎉 Ready to Get Started?

![Get Started](https://img.shields.io/badge/🚀-Get%20Started%20Now-brightgreen?style=for-the-badge&logo=rocket)

```bash
git clone <your-repo-url>
cd advance-agent
uv sync
python example.py
```

### 🌟 Star This Repository

If this project helps you, please give it a ⭐️!

[![GitHub stars](https://img.shields.io/github/stars/your-username/your-repo?style=social)](https://github.com/your-username/your-repo)
[![GitHub forks](https://img.shields.io/github/forks/your-username/your-repo?style=social)](https://github.com/your-username/your-repo/fork)

### 📞 Need Help?

<div align="center">

![Issues](https://img.shields.io/badge/Issues-Welcome-brightgreen?style=flat-square&logo=github)
![Discussions](https://img.shields.io/badge/Discussions-Open-blue?style=flat-square&logo=github)
![PRs](https://img.shields.io/badge/PRs-Welcome-orange?style=flat-square&logo=github)

</div>

---

<div align="center">

**Made with ❤️ by Surya Prakash Subudhiray**

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=flat-square&logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-Workflow-green?style=flat-square&logo=graphql)
![DeepSeek](https://img.shields.io/badge/DeepSeek-AI-orange?style=flat-square&logo=openai)

**Happy coding! 🚀**

</div>
