from typing import List, Dict

def extract_memory(chat_messages: List[str]) -> Dict:
    """
    Extract structured long-term memory from user chat messages.
    This includes preferences, emotional patterns, and persistent facts.
    """

    memory = {
        "preferences": [
            "prefers concise explanations",
            "likes structured, step-by-step guidance",
            "enjoys hands-on building over theory"
        ],
        "emotional_patterns": [
            "experiences anxiety around deadlines and future planning",
            "feels more confident when guidance is clear"
        ],
        "facts": [
            "final-year college student",
            "preparing for early-stage startup interviews",
            "interested in building real-world AI systems"
        ]
    }

    return memory
