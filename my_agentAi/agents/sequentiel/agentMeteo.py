from google.adk.agents import LlmAgent
from google.adk.models import LiteLlm
agent_meteo = LlmAgent(
    name="AgentMeteo",
    model = LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    instruction="""
You are a weather agent.

Destination info:
{search_result}

Provide weather conditions and best travel period.
""",
    output_key="weather_info"
)
