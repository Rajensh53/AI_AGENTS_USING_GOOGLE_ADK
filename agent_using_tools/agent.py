from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time() -> dict:
    """ Get the current time in the format YYYY-MM-DD HH:MM:SS """
    return{
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
def celsius_to_fahrenheit(celsius: float) -> dict:
    """Converts Celsius to Fahrenheit using the formula F = C * 9/5 + 32."""
    fahrenheit = celsius * (9/5) + 32
    return {"result": fahrenheit}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='agent_using_tools',
    description='A helpful tool-agent',
    instruction="""your are a helpful agent that can answer using following tools,
    - celsius_to_farenheit.""",
    # tools=[google_search]
    # tools=[get_current_time]
    tools=[celsius_to_fahrenheit]
)
