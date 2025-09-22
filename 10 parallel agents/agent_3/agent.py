from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

third_agent = Agent(
    name="agent_3",
    model="gemini-2.0-flash",
    description="Collects stock market news and global financial events",
    instruction="""You are step 3 in a stock market pipeline.
    Collect accurate, up-to-date financial news and global market events that may impact stocks.
    Focus on central bank announcements, geopolitical developments, sector news, and mergers/acquisitions.
    Present the information factually, without personal commentary or market predictions.
    Pass your findings to the next stage for deeper analysis.""",
    tools=[google_search]
)
