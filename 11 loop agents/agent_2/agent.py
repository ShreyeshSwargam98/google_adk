from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()

second_agent = Agent(
    name="agent_2",
    model="gemini-2.0-flash",
    description="Analyzes financial data collected by agent_1 and identifies key patterns or anomalies",
    instruction="""You are step 2 in the stock market pipeline.
    Take the financial data from agent_1 and:
    - Summarize major changes in revenue, EPS, or margins compared to prior quarters
    - Highlight whether results beat/missed analyst expectations
    - Identify trends in valuation metrics (e.g., P/E ratio changes)
    - Point out any red flags or unusual movements in filings
    
    Do not forecast or make investment advice.
    Instead, prepare a clear analytical summary to pass to the next agent."""
)
