from google.adk.agents import LlmAgent, sequential_agent

from .agentRecherche import agent_recherche
from .agentMeteo import agent_meteo
from .agentBudget import agent_budget
from .agentPaiment import agent_paiment
from .agentClient import agent_client

# Sequential workflow
travel_pipeline_agent = sequential_agent(
    name="TravelPipelineAgent",
    sub_agents=[
        agent_recherche,
        agent_meteo,
        agent_budget,
        agent_paiment,
        agent_client
    ],
    description="Travel planning pipeline with research, weather, budget, payment, and client response."
)

# Mandatory root agent
root_agent = travel_pipeline_agent
