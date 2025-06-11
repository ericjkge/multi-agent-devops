from google.adk.tools import ToolContext

def finalize_specs(requirements_doc: str, tool_context: ToolContext):  
    """
    Sets the specs_finalized flag to true and stores requirements_doc

    Args:
        requirements_doc (str): The finalized requirements document.
        tool_context (ToolContext): The context for the tool, which includes the state.

    Returns:
        None: This function does not return any value.

    """  
    # Set the specs_finalized flag  
    tool_context.state['specs_finalized'] = True  
      
    # Store the requirements document  
    tool_context.state['requirements_doc'] = requirements_doc  
      
    tool_context.actions.transfer_to_agent = "coding_agent"

    return None