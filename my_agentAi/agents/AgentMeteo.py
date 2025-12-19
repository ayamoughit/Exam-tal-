from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.llm_agent import Agent
from ..tools.Meteo import get_weather



meteo_agent = Agent(
    name="AgentMeteo",
   model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    description="Fournit des informations météo pour les destinations de voyage.",
    instruction="Tu es un expert météo. Lorsqu'on te donne une ville, "
                "utilise l'outil 'get_weather' pour obtenir les prévisions. "
                "Présente ensuite le rapport météo de manière claire au client.",
    tools=[get_weather],
)

print(f"Agent '{meteo_agent.name}' créé avec le modèle .")