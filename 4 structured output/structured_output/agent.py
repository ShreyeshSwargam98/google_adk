from google.adk.agents import Agent
from pydantic import BaseModel, Field

class Swiggy(BaseModel):
    price: int = Field(description='this is the price for food')
    food: str = Field(description='this is the food which you are checking out')

root_agent = Agent(
    name="structured_outputc",
    model="gemini-2.0-flash",
    description="first agent",
    instruction="""
        You are a Food Recommendation Assistant.
        Your task is to suggest food items along with their prices based on the user's request.

        GUIDELINES:
        - Suggest a specific food item in the 'food' field
        - Provide the price of the food item as an integer in the 'price' field
        - Keep suggestions realistic and relevant
        - Your response MUST be valid JSON matching the Swiggy schema:

        {
            "food": "Name of the food item",
            "price": 123s
        }

        DO NOT include any explanations or additional text outside the JSON response.
    """,
    output_schema=Swiggy,
    output_key='knowing the food'
)
