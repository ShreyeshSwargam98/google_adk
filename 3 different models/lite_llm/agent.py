from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime
import os
from google.adk.models.lite_llm import LiteLlm

def get_current_time():
    return {"current_time": datetime.now().strftime("%H:%M:%S %d-%m-%Y")}

openrouter_api_key = os.environ["OPENROUTER_API_KEY"]

model = LiteLlm(
    model="openrouter/deepseek/deepseek-chat-v3.1:free",
    api_key=openrouter_api_key,
    max_tokens=500 
)

root_agent = Agent(
    name="lite_llm",
    model= model,
    description="using different model",
    instruction="""You are a friendly and knowledgeable AI assistant.
    Answer user queries clearly, concisely, and truthfully.
    If unsure, state your uncertainty rather than guessing.
    Always try to be helpful and polite.""",
    # tools=[get_current_time] 
    tools=[google_search] 
)
