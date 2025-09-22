from google.adk.agents import LoopAgent
from .agent_1.agent import first_agent
from .agent_2.agent import second_agent

root_agent = LoopAgent(
    name="testing_parallel_agents",
    sub_agents=[first_agent, second_agent],
    max_iterations=3
)
