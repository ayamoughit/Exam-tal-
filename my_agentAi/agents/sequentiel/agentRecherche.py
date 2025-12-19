from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
agent_recherche = LlmAgent(
    name="AgentRecherche",
    model = LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    instruction="""
You are a travel research agent.
Based on the user's request, suggest destinations and basic travel info.
""",
    output_key="search_result"
)
