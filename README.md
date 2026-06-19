# Multi-Agent AI System 🤖

A powerful AI research assistant that uses multiple specialized agents to search, analyze, summarize, and generate reports automatically.

## Features

- 🔍 Search Agent for information gathering
- 🧠 Research Agent for analysis and reasoning
- ✍️ Writer Agent for report generation
- 📊 Structured workflow using LangGraph
- 🌐 Streamlit web interface
- 🤖 Supports OpenAI, Mistral, and other LLMs
- 📄 Generates comprehensive research reports

---

## Architecture

User Query
      │
      ▼
Search Agent
      │
      ▼
Research Agent
      │
      ▼
Writer Agent
      │
      ▼
Final Report

Each agent performs a specific task and passes its output to the next agent in the workflow.

---

## Tech Stack

- Python
- LangGraph
- LangChain
- Streamlit
- OpenAI API / Mistral API
- Tavily Search

---

## Project Structure

```text
multi-agent-ai-system/
│
├── agents/
│   ├── search_agent.py
│   ├── research_agent.py
│   └── writer_agent.py
│
├── app.py
├── graph.py
├── pipeline.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/multi-agent-ai-system.git

cd multi-agent-ai-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key

# OR

MISTRAL_API_KEY=your_mistral_key

TAVILY_API_KEY=your_tavily_key
```

---

## Running the Application

### Streamlit App

```bash
streamlit run app.py
```

Application will open at:

```text
http://localhost:8501
```

---

## Example Usage

Input:

```text
Latest advancements in Artificial Intelligence
```

Output:

```text
Research Report

1. Introduction
2. Key Developments
3. Industry Impact
4. Future Trends
5. Conclusion
```

---

## Workflow

### Search Agent

Responsibilities:

- Search the web
- Collect relevant information
- Return summarized findings

### Research Agent

Responsibilities:

- Analyze search results
- Extract important insights
- Organize information

### Writer Agent

Responsibilities:

- Generate final report
- Format content professionally
- Provide conclusions

---

## Deployment

### Streamlit Community Cloud

1. Push code to GitHub.
2. Open Streamlit Cloud.
3. Create a new app.
4. Connect GitHub repository.
5. Add API keys in Secrets.

Example:

```toml
OPENAI_API_KEY="your_key"
TAVILY_API_KEY="your_key"
```

---

## Troubleshooting

### API Key Error

Ensure:

```python
load_dotenv()
```

is called before accessing environment variables.

Verify:

```python
import os
print(os.getenv("OPENAI_API_KEY"))
```

---

### Streamlit Cloud Not Working

Check:

- requirements.txt contains all dependencies
- API keys added in Secrets
- Python version compatibility
- No hardcoded local file paths

---

## Future Improvements

- Memory support
- Agent-to-agent communication
- PDF report generation
- RAG integration
- Multi-modal inputs
- Voice interface
