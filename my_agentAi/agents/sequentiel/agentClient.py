from google.adk.agents import LlmAgent
from google.adk.models import LiteLlm
agent_client = LlmAgent(
    name="AgentClient",
    model = LiteLlm(model="ollama_chat/qwen2.5:7b-instruct"),
    instruction="""
You are a client-facing assistant.

Use the following info to respond clearly to the user:

Destination research:
{search_result}

Weather:
{weather_info}

Budget:
{budget}

Payment:
{payment_status}

Provide a final, friendly response.
""",
    output_key="final_response"
)
