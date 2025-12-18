from google.adk.agents.llm_agent import Agent
# @title 1. Import LiteLlm
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)