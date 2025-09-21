from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

second_agent = Agent(
    name="agent_2",
    model="gemini-2.0-flash",
    description="Analyzes sports data",
    instruction="""You are step 2 in a sports pipeline.
    Take the raw sports data and provide insights:
    - Explain trends and strengths/weaknesses
    - Compare player or team performances
    - Identify potential strategies
    Do not simplify for a general audience yet.
    Pass your structured analysis to the next agent.""",
    tools=[google_search]
)
