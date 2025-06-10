from google.adk.agents import SequentialAgent

from .sub_agents.planner.planning_agent import planning_agent

root_agent = SequentialAgent(
    name="root_agent",
    sub_agents=[planning_agent],
    description="An end-to-end DevOps automation pipeline",
)