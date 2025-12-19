from google.adk.agents import LlmAgent
from google.adk.models import LiteLlm
agent_budget = LlmAgent(
    name="AgentBudget",
   model= LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    instruction="""
You are a budget calculation agent.

Destination:
{search_result}

Weather info:
{weather_info}

Estimate a reasonable travel budget.
""",
    output_key="budget"
)
