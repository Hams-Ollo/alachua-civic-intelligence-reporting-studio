import requests
from bs4 import BeautifulSoup
from typing import Optional
from langchain_core.tools import tool
from tavily import TavilyClient
from src.config import TAVILY_API_KEY

# Initialize Tavily Client
tavily_client = TavilyClient(api_key=TAVILY_API_KEY) if TAVILY_API_KEY else None

@tool
def deep_research(query: str, max_results: int = 5) -> str:
    """
    Performs a deep web search using Tavily to find recent news, documents, and connections.
    Use this for broad "Analyst" questions like "What is the connection between Tara Forest and Mill Creek?".
    """
    if not tavily_client:
        return "Error: Tavily API Key not configured."
    
    try:
        response = tavily_client.search(query, search_depth="advanced", max_results=max_results)
        # Tavily returns a list of result objects. We'll format them as a string.
        results = []
        for r in response.get("results", []):
            results.append(f"Title: {r['title']}\nURL: {r['url']}\nContent: {r['content']}\n---")
        return "\n".join(results)
    except Exception as e:
        return f"Search failed: {e}"

@tool
def monitor_url(url: str) -> str:
    """
    Fetches the text content of a specific URL. 
    Use this for "Scout" tasks to read specific agendas or pages from the Source Registry.
    """
    try:
        # Basic User-Agent to avoid immediate blocking
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Simple text extraction - in Phase 2 we can swap this for Firecrawl
        # Remove scripts and styles
        for script in soup(["script", "style"]):
            script.extract()
            
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return clean_text[:20000] # Truncate massive pages to fit context if needed
    except Exception as e:
        return f"Failed to fetch {url}: {e}"
