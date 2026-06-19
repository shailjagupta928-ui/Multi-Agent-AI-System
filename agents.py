from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.agents import create_agent

from tools import web_search, scrape_url

load_dotenv()

# LLM Setup
llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7,
)

# Search Agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )

# Reader Agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )

# Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research writer. Write clear, structured, factual, and insightful reports."
    ),
    (
        "human",
        """
Write a detailed research report on the topic below.

Topic:
{topic}

Research Gathered:
{research}

Structure the report as:

1. Introduction

2. Key Findings
   - At least 3 detailed points

3. Conclusion

4. Sources
   - List all URLs found in the research

Be professional, accurate, and detailed.
"""
    )
])

writer_chain = writer_prompt | llm | StrOutputParser()

# Critic Chain
critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a strict research critic. Review reports honestly and provide constructive feedback."
    ),
    (
        "human",
        """
Review the following research report.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- Point 1
- Point 2

Areas to Improve:
- Point 1
- Point 2

One Line Verdict:
Your verdict here.
"""
    )
])

critic_chain = critic_prompt | llm | StrOutputParser()