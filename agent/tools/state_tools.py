from typing import Any

from google.adk.tools.tool_context import ToolContext

# Define scope levels for state keys
USER_NAME_SCOPE_LEVELS = ("temp", "user", "app")


def save_userinfo(
    tool_context: ToolContext, user_name: str, user_health_status: str
) -> dict[str, Any]:
    """
    Tool to record and save user name and country in session state.

    Args:
        user_name: The username to store in session state
        user_health_status: The student's possible health status
    Returns:
        A dictionary stating whether user info was successfully stored
    """
    tool_context.state["user:name"] = user_name
    tool_context.state["user:user_health_status"] = user_health_status

    return {"status": "success"}


def retrieve_userinfo(tool_context: ToolContext) -> dict[str, Any]:
    """
    Tool to retrieve user name and health status.
    """
    # Read from session state
    user_name = tool_context.state.get("user:name", "Username not found")
    user_health_status = tool_context.state.get(
        "user:user_health_status", "User status not found"
    )

    return {
        "status": "success",
        "user_name": user_name,
        "user_health_status": user_health_status,
    }
