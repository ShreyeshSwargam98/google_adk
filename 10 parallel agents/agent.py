from google.adk.agents import ParallelAgent
from .agent_1.agent import first_agent
from .agent_2.agent import second_agent
from .agent_3.agent import third_agent

root_agent = ParallelAgent(
    name="testing_parallel_agents",
    sub_agents=[first_agent, second_agent, third_agent]
)
