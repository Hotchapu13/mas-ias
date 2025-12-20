import os
import asyncio
from google.adk.agents import ParallelAgent, SequentialAgent, LlmAgent
from google.adk.models.lite_llm import LiteLlm # For multi-model support
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
# from tools import priority_solver, conflict_detector

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )

# Define specialized agents
scheduler = LlmAgent(
    name = 'scheduler',
    model='gemini-2.5-flash',
    description="Maximize time efficiency"
)

welfare = LlmAgent(
    name = "welfare",
    model='gemini-2.5-flash',
    description = "Ensure 8 hours sleep and mental breaks..."

)
academic = LlmAgent(
    name = "academic",
    model='gemini-2.5-flash',
    description = "Prioritize tasks with >20% grade weight..."
)

# Define the debate room
debate_room = ParallelAgent(
    name = "debate_room",
    sub_agents = [scheduler, welfare, academic]
)

# Define judge agent
judge = LlmAgent(
    name = "scoringAgent",
    model='gemini-2.5-flash',
    instruction="""Analyze the 3 proposals in 'debate_proposals'.
    Do not seek consensus. Score each rationale based on its alignment
    with the student's long-term success. Select the highest score."""
)

root_agent = SequentialAgent(
    name = 'MAS_IAS_orchestrator',
    sub_agents = [debate_room, judge]
)
