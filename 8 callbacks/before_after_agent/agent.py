from google.adk.agents import Agent


def before_agent_callback(callback_context=None):
    print('before agent callback')
    
def after_agent_callback(callback_context=None):
    print('after agent call back')

root_agent = Agent(
    name="before_after_agent",
    model="gemini-2.0-flash",
    description="simple agent",
    instruction="""You are a friendly and knowledgeable AI assistant.
    Answer user queries clearly, concisely, and truthfully.
    If unsure, state your uncertainty rather than guessing.
    Always try to be helpful and polite.""",
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback
)
