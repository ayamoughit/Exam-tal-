import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.llm_agent import Agent
from ..tools.Validateur_Email import validate_email




client_agent = Agent(
    name="AgentClient",
   model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    description="Agent chargé de valider l'identité du client via son email.",
    instruction="Tu es un assistant de vérification. Demande l'email de l'utilisateur. "
                "Utilise l'outil 'validate_email' pour vérifier s'il est correct. "
                "Si l'email est invalide, demande poliment une correction.",
    tools=[validate_email],
)

print(f"Agent '{client_agent.name}' créé avec le modèle .")