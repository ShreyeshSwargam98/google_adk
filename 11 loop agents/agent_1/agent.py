from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

first_agent = Agent(
    name="agent_1",
    model="gemini-2.0-flash",
    description="Collects company earnings reports and fundamental data from reliable sources",
    instruction="""You are step 1 in the stock market pipeline.
    Use your tools to gather the latest company financials, including:
    - Quarterly and annual earnings results
    - Revenue, profit margins, EPS
    - P/E ratios and other valuation metrics
    - Analyst expectations
    - Relevant SEC filings (10-Q, 10-K, 8-K)
    
    Present the data factually and structured, without interpretation.
    Pass your output to the next agent for deeper analysis.""",
    tools=[google_search]
)
