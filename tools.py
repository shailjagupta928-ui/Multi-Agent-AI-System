from langchain.tools import tool
from pydantic_core import Url
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
from bs4 import BeautifulSoup
import requests
from pydantic import AnyUrl

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information. Returns title, URL, and snippet."""

    results = tavily.search(query=query, max_results=5)

    out = []

    for r in results["results"]:
        title = r.get("title", "No title")
        url = r.get("url", "No URL")
        snippet = r.get("content", "")[:300]

        out.append(
            f"Title: {title}\nURL: {url}\nSnippet: {snippet}\n"
        )

    return "\n----\n".join(out)


#print(web_search.invoke("What are the recent news about war?"))



@tool
def scrape_url(url: str) -> str:
    """
    Scrape a webpage and return cleaned text content.
    """
    try:
        resp = requests.get(
            url,
            timeout=8,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:3000]

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"


# Test
print(
    scrape_url.invoke(
        "https://www.thehindu.com/news/national/world-suffers-from-shortage-of-trust-pm-modi-to-g7-leaders/article71110487.ece"
    )
)