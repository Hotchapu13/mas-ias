import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

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

scheduler_agent = LlmAgent(
    name="Scheduler",
    instruction="""
    You are an agent specialised only to use the information provided to you to generate a reading schedule based on the info provided to you 
"""
    model=model_config
)