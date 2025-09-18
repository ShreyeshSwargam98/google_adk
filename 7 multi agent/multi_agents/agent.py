from google.adk.agents import Agent
from google.adk.tools import AgentTool
from datetime import datetime
from .subagents.cricket_agent.cricket_agent import cricket_agent
from .subagents.news_agent.news_agent import news_agent
from .subagents.stock_agent.stock_agent import stock_agent

def get_current_time():
    return {"current_time": datetime.now().strftime("%H:%M:%S %d-%m-%Y")}

root_agent = Agent(
    name="multi_agents",
    model="gemini-2.0-flash",
    description="Helps with management tasks, scheduling, and updates",
    instruction="""
    You are a reliable and organized manager assistant.

    Responsibilities:
    - Provide clear and concise updates about the current time or date (use the `get_current_time` tool).
    - Summarize all responses in a structured and easy-to-read way.
    - Stay professional, polite, and supportive at all times.
    - If you are unsure, state your uncertainty instead of guessing.

    Subagent / Tool Routing:
    - If the query is cricket-related ➝ forward to `cricket_agent`.
    - If the query is news-related ➝ forward to `news_agent`.
    - If the query is stock-related ➝ forward to `stock_agent`.
    - If the query is about time/date ➝ use `get_current_time`.
    """,
    tools=[AgentTool(cricket_agent),
        AgentTool(news_agent),
        AgentTool(stock_agent), 
        get_current_time] 
)
