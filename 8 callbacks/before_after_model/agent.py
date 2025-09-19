from google.adk.agents import Agent

def before_model_callback(callback_context=None):
    print('before model callback')
    
def after_model_callback(callback_context=None):
    print('after model call back')

root_agent = Agent(
    name="before_after_model",
    model="gemini-2.0-flash",
    description="simple model",
    instruction="""You are a friendly and knowledgeable AI assistant.
    Answer user queries clearly, concisely, and truthfully.
    If unsure, state your uncertainty rather than guessing.
    Always try to be helpful and polite.""",
    before_agent_callback=before_model_callback,
    after_agent_callback=after_model_callback
)
