from langchain_openai import ChatOpenAI
import os

def get_llm():
    # Production best practice: Load API keys from environment variables
    return ChatOpenAI(
        model="gpt-4",
        temperature=0,  # 0 for factual accuracy, >0 for creativity
        api_key=os.getenv("")
    )