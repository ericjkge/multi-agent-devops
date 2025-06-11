from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types # For types.Content

from typing import Optional


# --- Before Agent Callback ---
def before_coding_agent(callback_context: CallbackContext) -> Optional[types.Content]:
    """
    Callback that restricts code generation until the Planning Agent has ended.
    Args:
        state (dict): The current state of the agent, which should include the specifications from the Planning Agent.

    Returns:
        dict: A dictionary indicating whether the Coding Agent should cancel its operation.
    """

    if not callback_context.state.get('specs_finalized', False):
        return types.ModelContent(parts=[""])
    return None

# --- Create Coding Agent ---
coding_agent = LlmAgent(
    name="coding_agent",
    model="gemini-2.0-flash",
    description="Generates code based on structured specifications from the Planning Agent",
    instruction="""
    You are the Coding Agent in a multi-agent DevOps system.
    Your purpose is to take structured specifications from the Planning Agent and generate implementation-ready code.

    GUIDELINES:
    - DO NOT respond until you have received {specs}.
    - Read the provided JSON specification {specs} carefully.
    - Generate clean, modular, and well-documented code based on the specification.
    - Ensure the code is ready for deployment into a web application.
    
    IMPORTANT: Your final and only output MUST be valid Python code that implements the specified feature, enclosed in triple backticks like this:

    ```python...```

    DO NOT include any explanations or additional text outside the code response for your final output.
    """,
    output_key="code",
    before_agent_callback=before_coding_agent
)