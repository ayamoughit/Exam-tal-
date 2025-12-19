from google.adk.agents.llm_agent import Agent
# @title 1. Import LiteLlm
from google.adk.models.lite_llm import LiteLlm

# Import des sous-agents
from .agents.AgentMeteo import meteo_agent
from .agents.AgentBudget import budget_agent
from .agents.AgentClient import client_agent
from .agents.AgentPaiement import paiement_agent
from .agents.AgentRecherche import recherche_agent
from .agents.sequentiel.sequentiel_agent import travel_pipeline_agent

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Tu es un assistant de voyage. Route les demandes vers les agents spécialisés : '
                'météo, budget, validation client, paiement ou recherche touristique.',
    sub_agents=[meteo_agent, budget_agent, client_agent, paiement_agent, recherche_agent, travel_pipeline_agent],
)