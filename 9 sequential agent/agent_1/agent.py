from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

first_agent = Agent(
    name="agent_1",
    model="gemini-2.0-flash",
    description="Collects factual sports data",
    instruction="""You are step 1 in a sports pipeline.
    Collect accurate, up-to-date sports data relevant to the user’s query.
    Focus on stats, match results, player performance, and key highlights.
    Present the information factually, without interpretation.
    Pass your findings to the next agent for deeper analysis.""", 
    tools=[google_search]
)
