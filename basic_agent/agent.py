from google.adk.agents import Agent

root_agent = Agent(
    name ="basic_agent",
    model = "gemini-2.5-flash-lite",
    description = "A basic agent that answers basic questions.",
    instruction="Answer the user's questions to the best of your ability."

)