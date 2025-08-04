import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Check API key
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key found: {'Yes' if api_key else 'No'}")
if api_key:
    print(f"API Key starts with: {api_key[:7]}...")
    print(f"API Key length: {len(api_key)}")

# Test the LLM
try:
    llm = ChatOpenAI(model='gpt-4o', api_key=api_key)
    response = llm.invoke("Say hello!")
    print(f"LLM test successful: {response.content}")
except Exception as e:
    print(f"LLM test failed: {e}")