import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Page Configuration must be the first Streamlit command
st.set_page_config(
    page_title="Gemini Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for UI/UX improvements
st.markdown("""
<style>
    .stChatFloatingInputContainer {
        padding-bottom: 20px;
    }
    .hero-container {
        text-align: center;
        padding: 2rem 0;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def init_environment():
    """Load environment variables and configure Gemini API."""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("GEMINI_API_KEY is not set. Please add it to your .env file or environment variables.")
        st.stop()
    genai.configure(api_key=api_key)

def init_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def sidebar_settings():
    """Render the sidebar with settings and actions."""
    with st.sidebar:
        st.title("⚙️ Settings")
        
        # Model Selection
        model_options = ['gemini-3.5-flash', 'gemini-3.5-flash-lite']
        selected_model = st.selectbox("Select Model", options=model_options, index=0)
        
        # Temperature Slider
        temperature = st.slider(
            "Temperature", 
            min_value=0.0, max_value=1.0, value=0.7, step=0.1,
            help="Higher values make output more random, lower values make it more focused and deterministic."
        )
        
        st.divider()
        
        # Clear Chat Button
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
            
    return selected_model, temperature

def render_empty_state():
    """Render a welcoming empty state if no messages exist."""
    st.markdown("""
        <div class="hero-container">
            <div class="hero-title">🤖 Gemini AI Assistant</div>
            <div class="hero-subtitle">Ask me anything, brainstorm ideas, or write code together.</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **Idea**: Explain quantum computing in simple terms.")
    with col2:
        st.info("💻 **Idea**: Write a Python script to scrape a website.")

def render_chat_history():
    """Display chat messages from history on app rerun."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(model_name: str, temperature: float):
    """React to user input and generate response from Gemini."""
    if prompt := st.chat_input("Type your message here..."):
        # Display user message
        st.chat_message("user").markdown(prompt)
        # Add to history
        st.session_state.messages.append({"role": "user", "content": prompt})

        try:
            # Prepare generation config
            generation_config = genai.types.GenerationConfig(
                temperature=temperature,
            )
            
            # Setup model
            model = genai.GenerativeModel(model_name)
            
            # Format history for Gemini
            history = []
            for msg in st.session_state.messages[:-1]:
                role = "user" if msg["role"] == "user" else "model"
                history.append({"role": role, "parts": [msg["content"]]})
            
            # Generate response
            chat = model.start_chat(history=history)
            response = chat.send_message(prompt, generation_config=generation_config)

            # Display and save assistant response
            with st.chat_message("assistant"):
                st.markdown(response.text)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")
            # Remove the last user message if generation failed
            if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
                st.session_state.messages.pop()

def main():
    init_environment()
    init_session_state()
    
    selected_model, temperature = sidebar_settings()
    
    # Render main content
    if not st.session_state.messages:
        render_empty_state()
    else:
        # We still want to show the title even if chat has started
        st.title("🤖 Gemini AI Assistant")
        
    render_chat_history()
    handle_user_input(selected_model, temperature)

if __name__ == "__main__":
    main()
