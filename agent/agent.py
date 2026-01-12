import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools.agent_tool import AgentTool

from .debateAgents.AcademicAgent.agent import academic_priority_agent as academic
from .debateAgents.SchedulerAgent.agent import scheduler_agent as scheduler
from .debateAgents.WelfareAgent.agent import welfare_agent as welfare

#load environment variables
load_dotenv()

# Get api key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError(
        "Set GOOGLE_API_KEY in environment variables"
    )

# Configure the model to use gemini with api key
model_config = Gemini(model="gemini-2.0-flash", api_key=api_key)

main = Agent(
    name="Entry",
    instruction="""You are the uniplan scheduling Assistant, a comprehensive academic welfare support system. You coordinate between different specialists to provide the best possible academic schedule to help the student study for their exams and tests without mental stress.
    
    """,
    description="Main uniplan agent for coordinating debate between the scheduling sub agents",
    model=model_config, 
    tools = [AgentTool(agent=academic),AgentTool(agent=welfare),AgentTool(agent=scheduler)],
)