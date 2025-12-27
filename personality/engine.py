from .prompts import CALM_MENTOR, THERAPIST_STYLE

def generate_response(user_input: str, personality: str) -> str:
    """
    Generate a response based on the selected personality.
    This function simulates personality-based behavior.
    """

    if personality == "calm_mentor":
        return (
            "I hear you. Let's slow things down and look at this step by step. "
            "With clear structure and steady progress, you can handle this."
        )

    if personality == "therapist_style":
        return (
            "It sounds like you're feeling uncertain and maybe overwhelmed. "
            "That feeling makes sense, and it's okay to take time to reflect on what you're experiencing."
        )

    # Default response
    return "I'm here to help. Tell me more about what's on your mind."
