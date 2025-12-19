import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.llm_agent import Agent



paiement_agent = Agent(
    name="AgentPaiement",
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    description="Gère la finalisation et la simulation du paiement.",
    instruction="Tu es l'agent de clôture. Une fois que tout est validé, "
                "récapitule le voyage et simule la réussite de la transaction "
                "de manière professionnelle et rassurante.",
    tools=[],
)

print(f"Agent '{paiement_agent.name}' créé avec le modèle .")