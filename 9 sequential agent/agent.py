from google.adk.agents import SequentialAgent
from .agent_1.agent import first_agent
from .agent_2.agent import second_agent
from .agent_3.agent import third_agent

root_agent = SequentialAgent(
    name="sequential_agents_testing",
    sub_agents=[first_agent, second_agent, third_agent]
)
