from typing import Dict

# Simple in-memory store for user memory
_MEMORY_STORE: Dict = {}

def save_memory(memory: Dict) -> None:
    """
    Save extracted memory into the store.
    """
    global _MEMORY_STORE
    _MEMORY_STORE = memory


def load_memory() -> Dict:
    """
    Load memory from the store.
    """
    return _MEMORY_STORE
