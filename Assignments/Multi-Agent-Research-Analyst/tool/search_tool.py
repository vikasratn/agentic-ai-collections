from langchain_community.tools.tavily_search import TavilySearchResults

class SearchTool():
    
    def __init__(self) -> None:
        search_tool = TavilySearchResults(k=3)
