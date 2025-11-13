from google.adk.agents import Agent 
from google.adk.models.lite_llm import LiteLlm
import os 

model = LiteLlm(
    model="openrouter/openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY")
)   

root_agent = Agent(
    name="litellm_agent",
    model=model,
    description="A motivational assistant agent.",
    instruction="You are a motivational assistant who provides encouraging and uplifting messages to users seeking inspiration.",

)