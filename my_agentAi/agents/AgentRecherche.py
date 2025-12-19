import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.llm_agent import Agent
from ..tools.Recherche_Activites import search_activities



recherche_agent = Agent(
    name="AgentRecherche",
 model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    description="Propose des activités et des lieux touristiques.",
    instruction="Tu es un guide touristique expert. Ta mission est de proposer "
                "les meilleures activités, monuments et expériences locales selon "
                "la destination et les goûts de l'utilisateur. Utilise l'outil 'search_activities' pour obtenir la liste des activités.",
    tools=[search_activities], 
)

print(f"Agent '{recherche_agent.name}' créé avec le modèle .")