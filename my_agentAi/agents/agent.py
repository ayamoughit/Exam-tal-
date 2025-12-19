import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.models.lite_llm import LiteLlm

# Import des sous-agents (imports absolus)
from agents.AgentMeteo import meteo_agent
from agents.AgentBudget import budget_agent
from agents.AgentClient import client_agent
from agents.AgentPaiement import paiement_agent
from agents.AgentRecherche import recherche_agent

# 1) Ajout d'un agent séquentiel "parmi" les sub_agents
#    Il regroupe (Client -> Budget -> Meteo) par exemple, puis laisse le reste au routing normal.
travel_sequence_agent = SequentialAgent(
    name="travel_sequence_agent",
    description="Pipeline déterministe: Client -> Budget -> Meteo (avant le reste).",
    sub_agents=[client_agent, budget_agent, meteo_agent],
)

# 2) Root agent conserve la liste d'agents existante, et on ajoute le séquentiel dedans
root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    name="root_agent",
    description="Assistant de voyage intelligent avec plusieurs spécialités.",
    instruction="""
Tu es un assistant de voyage.

Routage:
- Si la demande nécessite une préparation complète (collecte/validation client + estimation budget + météo),
  appelle `travel_sequence_agent`.
- Sinon, route vers l'agent spécialisé approprié:
  - AgentMeteo pour les questions météo
  - AgentBudget pour les calculs de budget
  - AgentClient pour la validation email
  - AgentPaiement pour finaliser les paiements
  - AgentRecherche pour les activités touristiques

Règle: si l'utilisateur demande une planification de voyage "de A à Z", privilégie `travel_sequence_agent`.
""",
    sub_agents=[
        meteo_agent,
        budget_agent,
        client_agent,
        paiement_agent,
        recherche_agent,
        travel_sequence_agent,  # <-- ajouté "parmi" eux
    ],
)