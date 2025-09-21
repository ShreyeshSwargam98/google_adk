from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time():
    return {"current_time": datetime.now().strftime("%H:%M:%S %d-%m-%Y")}

root_agent = Agent(
    name="first_agent",
    model="gemini-2.0-flash",
    description="tools",
    instruction="""You are a friendly and knowledgeable AI assistant.
    Answer user queries clearly, concisely, and truthfully.
    If unsure, state your uncertainty rather than guessing.
    Always try to be helpful and polite.""",
    # tools=[get_current_time] 
    tools=[google_search] 
)
