import os
import sys

from langchain_openai import ChatOpenAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from dotenv import load_dotenv

from browser_use import Agent, Browser, Controller, SystemPrompt

# Load environment variables from .env file
load_dotenv()


class CustomSystemPrompt(SystemPrompt):
	def important_rules(self) -> str:
		existing_rules = super().important_rules()
		custom_rules = """

CUSTOM RULES:
- Always be thorough and methodical in your approach
- Take screenshots when navigating to verify you're on the right page
- If you encounter any errors, try alternative approaches
- Be specific about what you find and report details clearly
"""
		return f'{existing_rules}\n{custom_rules}'


# Video: https://preview.screen.studio/share/8Elaq9sm
async def main():
	# Persist the browser state across agents
	
	# Check if API key is loaded
	api_key = os.getenv('OPENAI_API_KEY')
	if not api_key:
		raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")
	
	print(f"API Key loaded: {api_key[:10]}..." if api_key else "No API key found")

	browser = Browser()
	async with await browser.new_context() as context:
		model = ChatOpenAI(
			model='gpt-4o',
			api_key=api_key,
			temperature=0.1
		)

		# Initialize browser agent
		agent1 = Agent(
			task='Open 2 tabs with wikipedia articles about the history of the meta and one random wikipedia article.',
			llm=model,
			browser_context=context,
			system_prompt_class=CustomSystemPrompt,
		)
		agent2 = Agent(
			task='Considering all open tabs give me the names of the wikipedia article.',
			llm=model,
			browser_context=context,
			system_prompt_class=CustomSystemPrompt,
		)
		await agent1.run()
		await agent2.run()


asyncio.run(main())
