import streamlit as st
from rag import query_with_rag
from PIL import Image
import os

# === CONFIG ===
st.set_page_config(page_title="ProfessorNav", page_icon="🛰️", layout="wide")

# === SIDEBAR ===
with st.sidebar:
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
        st.image(logo, width=200)
    
    st.markdown("### 🔧 LLM Settings")
    temperature = st.slider("Temperature (creativity)", min_value=0.0, max_value=1.5, value=0.7, step=0.1)
    st.markdown("**Your GNSS AI Assistant**")
    st.markdown("_Trained by Imtiaz Nabi_")
    st.markdown("---")
    st.markdown("Ask technical questions about GNSS theory, algorithms, satellite data, or coding in Python, C, C++, and Rust.")

# === SESSION STATE FOR CHAT HISTORY ===
if "messages" not in st.session_state:
    st.session_state.messages = []

# === RENDER CHAT HISTORY ===
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# === USER INPUT ===
user_input = st.chat_input("What do you want to know...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Hmm... let me think..."):
            try:
                answer, sources = query_with_rag(user_input, k=3, temperature=temperature)

                # Format sources
                sources_text = "\n".join(f"- `{src.get('source', 'unknown')}`" for src in sources)
                full_reply = f"{answer}\n\n---\n**Sources:**\n{sources_text}"

                st.markdown(answer, unsafe_allow_html=False)

                # Save assistant message
                st.session_state.messages.append({"role": "assistant", "content": full_reply})

            except Exception as e:
                error_msg = f"❌ Error: {e}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
