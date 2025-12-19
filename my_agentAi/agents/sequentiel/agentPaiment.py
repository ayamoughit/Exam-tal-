from google.adk.agents import LlmAgent
from google.adk.models import LiteLlm
agent_paiment = LlmAgent(
    name="AgentPaiment",
   model = LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    instruction="""
You are a payment simulation agent.

Proposed budget:
{budget}

Simulate payment confirmation (success or failure).
""",
    output_key="payment_status"
)
