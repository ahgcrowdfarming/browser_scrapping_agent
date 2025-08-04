import asyncio
import os
from langchain_openai import ChatOpenAI
from browser_use import Agent

# Set your OpenAI API key
# os.environ['OPENAI_API_KEY'] = 'your-api-key-here'

async def main():
    # Initialize the language model
    llm = ChatOpenAI(model='gpt-4o')
    
    # Create the agent with your task
    agent = Agent(
        task="Your task description here",
        llm=llm,
        use_vision=True,  # Enable vision capabilities
        headless=False,   # Set to True to run without browser UI
    )
    
    # Run the agent
    result = await agent.run(max_steps=10)
    
    # Print results
    print("Final result:", result.final_result())
    print("Errors:", result.errors())

if __name__ == '__main__':
    asyncio.run(main())