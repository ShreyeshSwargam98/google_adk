from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()

def ipl():
    return {'message': 'There are 10 teams in ipl chennai super kings, mumbai indians, royal challengers banglore, sunrisers hyderabad, luncknow super giants, kings 11 punjab, delhi capitals, rajasthan royals, gujarat titans, kolkata knight riders. Mumbai indians & chennai super kings both have 5 trophies, followed by kolkata knight riders having 3 cups & remaining teams having 1 cup or trophy each.'}

cricket_agent = Agent(
    name="cricket_agent",
    model="gemini-2.0-flash",
    description="Provides cricket knowledge and updates",
    instruction="""You are a friendly cricket assistant.
    - Answer queries about cricket rules, players, and tournaments like IPL, World Cup, etc.
    - When answering, be clear, concise, and factually correct.
    - If a user asks for IPL teams or trophies, call the `ipl` tool.
    - If you are unsure, politely mention it.
    - Always explain cricket terms in simple language if the user might be a beginner.""",
    tools=[ipl]
)
