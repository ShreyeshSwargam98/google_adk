import asyncio
import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from session.agent import session_agent


async def main():
    load_dotenv()
    
    first_session_setup = InMemorySessionService()
    
    initial_stage = {
        'user_name': 'shreyesh swargam',
        'user_preferences':'i am shreyesh & i like to watch ipl & my favourite teams in ipl first is chennai super kings, then second favorite is mumbai indians'
    }
    
    APP_NAME = 'ipl league'
    USER_ID = 'shreyesh'
    SESSION_ID = str(uuid.uuid4())
    
    creation_session = await first_session_setup.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_stage,
        session_id=SESSION_ID
    )
    
    message = types.Content(
        role="user", parts=[types.Part(text="What is Shreyesh favorite IPL team?")]
    )
    
    runner = Runner(
        app_name=APP_NAME,
        agent=session_agent,
        session_service=first_session_setup
    )
    
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=message
    ):
        if event.content and event.content.parts:
            print(f'answer {event.content.parts[0].text}')
    
    getting_session = await first_session_setup.get_session(
        app_name=APP_NAME, user_id=USER_ID,session_id=SESSION_ID
    )
    
    for key,val in getting_session.state.items():
        print(f'values getting {key}: {val}')

if __name__ == "__main__":
    asyncio.run(main())











# async def main():
#     load_dotenv()

#     session_service_stateful = InMemorySessionService()

#     initial_state = {
#         "user_name": "Brandon Hancock",
#         "user_preferences": """
#             I like to play Pickleball, Disc Golf, and Tennis.
#             My favorite food is Mexican.
#             My favorite TV show is Game of Thrones.
#             Loves it when people like and subscribe to his YouTube channel.
#         """,
#     }

#     APP_NAME = "Brandon Bot"
#     USER_ID = "brandon_hancock"
#     SESSION_ID = str(uuid.uuid4())

#     stateful_session = await session_service_stateful.create_session(
#         app_name=APP_NAME,
#         user_id=USER_ID,
#         session_id=SESSION_ID,
#         state=initial_state,
#     )
#     print(f"CREATED NEW SESSION ID: {SESSION_ID}")

#     runner = Runner(
#         agent=session_agent,
#         app_name=APP_NAME,
#         session_service=session_service_stateful,
#     )

#     new_message = types.Content(
#         role="user", parts=[types.Part(text="What is Brandon's favorite TV show?")]
#     )

#     for event in runner.run(
#         user_id=USER_ID,
#         session_id=SESSION_ID,
#         new_message=new_message,
#     ): 
#         if event.content and event.content.parts:
#                 print(f"Final Response: {event.content.parts[0].text}")

#     print("==== Session Event Exploration ====")
#     session = await session_service_stateful.get_session(
#         app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
#     )

#     print(f"=== Final Session State === {session}")
#     for key, value in session.state.items():
#         print(f"{key}: {value}")
        
    

# if __name__ == "__main__":
#     asyncio.run(main())
