from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

second_agent = Agent(
    name="agent_2",
    model="gemini-2.0-flash",
    description="Collects company earnings reports and fundamental data",
    instruction="""You are step 2 in a stock market pipeline.
    Gather the latest company earnings reports, revenue, profit margins, P/E ratios, and other financial fundamentals.
    Include quarterly/annual earnings results, analyst expectations, and any relevant SEC filings.
    Present the information factually, without interpretation or forecasting.
    Pass your findings to the next agent for deeper analysis.""",
    tools=[google_search]
)
