from pydantic import BaseModel, Field
from google.adk.agents import Agent
from typing import Optional, List

from dotenv import load_dotenv
load_dotenv()


class BlogPostSchema(BaseModel):
    topic: str = Field(..., description="Topic provied by user")
    ideas: List[str] = Field(..., description="List of cretive blog post title ideas")

root_agent = Agent(
    name='blog_writer_agent',
    model='gemini-2.5-flash',   
    description='An agent that generates creative blog post title ideas based on a given topic.',
    instruction="""You are a blog writer agent that generates creative and engaging blog post title ideas based on the topic provided by the user. Your task is to come up with a list of unique and interesting titles that would attract readers to click and read the blog post.""",
    output_schema=BlogPostSchema,
    output_key='ideas'
)
