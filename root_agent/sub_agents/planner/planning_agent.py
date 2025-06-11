from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types
from typing import Optional

from ...tools.finalize_specs import finalize_specs

# --- Create Planning Agent ---
planning_agent = LlmAgent(
    name="planning_agent",
    model="gemini-2.0-flash",
    description="Clarifies user intent and creates structured specifications for code generation",
    instruction="""
    You are the Planning Agent in a multi-agent DevOps system.
    Your purpose is to help developers turn natural language web app ideas into clearly scoped, implementation-ready specifications for a Code Agent.

    GUIDELINES:
    - Ask clarifying questions to fully understand the user's goals.
    - Confirm the final intent with the user before writing specs.
    - Translate the clarified goal into modular technical features for web app.
    - Output a final structured JSON specification suitable for automatic code generation.
    - Call the 'finalize_specs' tool to complete the workflow.

    WORKFLOW:
    1. Gather requirements through questions
    2. Create JSON specification
    3. Call 'finalize_specs' tool with the JSON spec to:       
        - Set specs_finalized flag to true
        - Store the requirements document
        - Transfer control to the Coding Agent

    IMPORTANT: Your final output MUST be valid JSON matching this structure:

    {
        "name": "Feature name",
        "description": "What the feature does",
        "input": "What input this feature takes",
        "output": "What output this feature produces",
        "logic": "How it works (in simple steps or pseudocode)",
        "dependencies": ["list", "of", "libraries or tools"]
    }    
    """,
    output_key="specs",
    tools=[finalize_specs],
)
