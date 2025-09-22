from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

first_agent = Agent(
    name="agent_1",
    model="gemini-2.0-flash",
    description="Collects up-to-date stock prices and index movements",
    instruction="""You are step 1 in a stock market pipeline.
    Collect accurate, real-time data on stock prices, market indices, and trading volumes.
    Focus on major indices (e.g., S&P 500, Nasdaq, Dow Jones) and any specific tickers mentioned in the user’s query.
    Present the information factually, without interpretation or prediction.
    Pass your findings to the next agent for deeper analysis.""",
    tools=[google_search]
)
