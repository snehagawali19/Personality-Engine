import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


import streamlit as st

from personality.engine import generate_response
from memory.extractor import extract_memory
from memory.store import save_memory, load_memory


st.set_page_config(page_title="AI Companion Demo", layout="centered")

st.title("AI Companion – Memory & Personality Demo")

st.markdown(
    "This demo shows how an AI companion extracts memory from conversations "
    "and adapts its responses based on personality."
)

# ----------------------------
# Sample chat history
# ----------------------------
sample_chats = [
    "I feel anxious about my future.",
    "I prefer clear and structured guidance.",
    "I enjoy working on AI projects."
]

# ----------------------------
# Memory Extraction
# ----------------------------
if st.button("Extract Memory from Sample Chats"):
    memory = extract_memory(sample_chats)
    save_memory(memory)
    st.success("Memory extracted and stored.")

st.subheader("Stored Memory")
memory = load_memory()
if memory:
    st.json(memory)
else:
    st.info("No memory stored yet. Click 'Extract Memory'.")

# ----------------------------
# Personality Response
# ----------------------------
st.subheader("Personality-Based Response")

user_input = st.text_input(
    "User Input",
    placeholder="e.g., I feel stuck and unsure about my next step."
)

personality = st.selectbox(
    "Select Personality",
    ["calm_mentor", "therapist_style"]
)

if st.button("Generate Response") and user_input:
    response = generate_response(user_input, personality)
    st.markdown("### Response")
    st.write(response)
