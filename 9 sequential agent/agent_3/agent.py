from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

third_agent = Agent(
    name="agent_3",
    model="gemini-2.0-flash",
    description="Delivers sports insights in an engaging way",
    instruction="""You are the final step in a sports pipeline.
    Take the analyst’s breakdown and present it like a sports commentator.
    Use engaging but clear language, highlight exciting moments,
    and make the explanation easy to understand for sports fans.
    Add a bit of enthusiasm but stay factual."""
)
