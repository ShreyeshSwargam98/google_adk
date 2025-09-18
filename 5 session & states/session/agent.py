from google.adk.agents import Agent

session_agent = Agent(
    name="session",
    model="gemini-2.0-flash",
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)