from google.adk.agents import Agent

root_model = Agent(
    name = 'first_agent',
    model = 'gemini-2.0-flash',
    description='first agent',
    instruction="""You are a friendly and knowledgeable AI assistant.
    Answer user queries clearly, concisely, and truthfully.
    If unsure, state your uncertainty rather than guessing.
    Always try to be helpful and polite."""
)