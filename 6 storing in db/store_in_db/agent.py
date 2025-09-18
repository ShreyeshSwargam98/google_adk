from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from google.adk.tools import google_search
import uuid
import asyncio
from google.genai import types

# 1. Connect session service to PostgreSQL
session_service = DatabaseSessionService(
    db_url="postgresql://postgres:root@localhost:5432/googl_adk_db"
)

# 2. Create an Agent
agent = Agent(
    name="pg_agent",
    model="gemini-2.0-flash",
    description="Agent with Postgres session",
    instruction="You are a helpful AI assistant.",
    tools=[google_search],
)

# 3. Create Runner with the Postgres session service
runner = Runner(
    app_name='testing purpose',
    agent=agent,
    session_service=session_service
)
# 4. Run once (simple example)
async def main():
    message = types.Content(
        role="user", parts=[types.Part(text="What is the latest AI news?")]
    )
    session_id = str(uuid.uuid4())

    async for event in runner.run_async(
        session_id=session_id,
        new_message=message,
        user_id='testing man'
    ):
        print(event) 

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())
