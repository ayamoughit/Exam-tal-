import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.llm_agent import Agent
from ..tools.Calculateur_de_Budget import calculate_budget


budget_agent = Agent(
    name="AgentBudget",
   model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    description="Calcule le budget prévisionnel pour le séjour.",
    instruction="Tu es un conseiller financier de voyage. Utilise l'outil 'calculate_budget' "
                "pour estimer les frais d'hébergement en fonction du nombre de nuits.",
    tools=[calculate_budget],
)

print(f"Agent '{budget_agent.name}' créé avec le modèle .")