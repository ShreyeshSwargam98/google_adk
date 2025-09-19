from google.adk.agents import Agent
from google.adk.tools import google_search

def before_tool_callback(callback_context=None):
    print('before tool callback')
    
def after_tool_callback(callback_context=None):
    print('after tool call back')

root_agent = Agent(
    name="before_after_tool",
    model="gemini-2.0-flash",
    description="simple tool",
    instruction="""You are a friendly and knowledgeable AI assistant.
    Answer user queries clearly, concisely, and truthfully.
    If unsure, state your uncertainty rather than guessing.
    Always try to be helpful and polite.""",
    tools=[google_search],
    before_agent_callback=before_tool_callback,
    after_agent_callback=after_tool_callback
)
