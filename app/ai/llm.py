from langchain_anthropic import ChatAnthropic
from app.config import api_key

def generate_response(query: str) -> str:
    llm = ChatAnthropic(
        model="claude-haiku-4-5-20251001",
        api_key=api_key
    )
    response = llm.invoke(query)
    return response.content