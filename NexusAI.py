import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set page configuration
st.set_page_config(page_title="Nexus A.I.", layout="wide")

## CSS for styling
st.markdown("""
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #121212;
        color: #e0e0e0;
    }
    .centered-title {
        text-align: center;
        font-size: 2.5em;
        color: #1E90FF;
        margin-bottom: 20px;
    }
    .user-message, .assistant-message {
        padding: 10px;
        border-radius: 15px;
        margin: 5px 0;
        position: relative;
        background-color: #333;
        color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
        transition: background-color 0.3s, transform 0.3s;
    }
    .user-message {
        background-color: #444;
        text-align: left;
    }
    .assistant-message {
        background-color: #555;
        text-align: left;
    }
    .user-message:hover, .assistant-message:hover {
        background-color: #666;
        transform: scale(1.02);
    }
    .message-options {
        position: absolute;
        top: 5px;
        right: 10px;
        cursor: pointer;
        background: transparent;
        border: none;
        color: #fff;
        font-size: 16px;
    }
    .message-options-content {
        display: none;
        position: absolute;
        right: 0;
        background-color: #444;
        min-width: 120px;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.5);
        z-index: 1;
        border-radius: 10px;
    }
    .message-options-content a {
        color: #fff;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
    }
    .message-options-content a:hover {background-color: #555}
    .show {display: block;}
    .tab-content {
        border: 1px solid #666;
        padding: 10px;
        margin: 5px 0;
        border-radius: 10px;
        background-color: #222;
    }
    .chat-history {
        border: 1px solid #666;
        padding: 10px;
        margin: 5px 0;
        border-radius: 10px;
        background-color: #222;
    }
    .chat-tab {
        cursor: pointer;
        padding: 10px;
        margin: 5px 0;
        border-radius: 10px;
        background-color: #333;
        transition: background-color 0.3s;
    }
    .chat-tab:hover {
        background-color: #444;
    }
    .chat-tab.active {
        background-color: #555;
    }
    .three-dots {
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }
    .three-dots span {
        height: 6px;
        width: 6px;
        background-color: #fff;
        border-radius: 50%;
        display: inline-block;
        margin: 0 2px;
    }
    .chat-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px;
        border-bottom: 1px solid #444;
        background-color: #222;
        border-radius: 10px;
    }
    .chat-item:hover {
        background-color: #333;
    }
    .chat-item .delete-btn {
        background-color: transparent;
        border: none;
        color: #e74c3c;
        font-size: 18px;
        cursor: pointer;
    }
    .chat-item .delete-btn:hover {
        color: #c0392b;
    }
    .timestamp {
        font-size: 0.75em;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Set default OpenAI model if not in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o-mini"

# Initialize chat messages in session state if not already set
if "messages" not in st.session_state:
    st.session_state.messages = []

# Deleting chat history function
def delete_chat(index):
    st.session_state.chats.pop(index)
    if len(st.session_state.chats) > 0:
        st.session_state.messages = st.session_state.chats[-1]["messages"]
    else:
        st.session_state.messages = []
    st.experimental_rerun()

# Context-based Chat Name Function
def determine_chat_context(messages):
    if not messages:
        return "Empty Chat"
    first_message = messages[0]["content"]
    context_name = first_message[:15] + "..." if len(first_message) > 15 else first_message
    return context_name

# Start New Chat Function
def start_new_chat():
    if "chats" not in st.session_state:
        st.session_state.chats = []
    context_name = determine_chat_context(st.session_state.messages)
    st.session_state.chats.append({"context": context_name, "messages": st.session_state.messages})
    st.session_state.messages = []

# Dark Theme Default
st.markdown('<style>body { background-color: #121212; color: #e0e0e0; }</style>', unsafe_allow_html=True)

# Display the app title
st.markdown('<h1 class="centered-title">Nexus A.I.</h1>', unsafe_allow_html=True)

# Sidebar for new chat and chat history
with st.sidebar:
    st.markdown("## Actions")
    st.button("Start New Chat", on_click=start_new_chat)

    st.markdown("## Chat History")
    if "chats" in st.session_state and st.session_state.chats:
        for i, chat in enumerate(st.session_state.chats):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f'''
                    <div class="chat-item">
                        <span>{chat["context"]}</span>
                    </div>
                ''', unsafe_allow_html=True)
            with col2:
                if st.button("🗑️", key=f"delete_{i}"):
                    delete_chat(i)

# Display existing chat messages
for i, message in enumerate(st.session_state.messages):
    css_class = "user-message" if message["role"] == "user" else "assistant-message"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with st.chat_message(message["role"]):
        st.markdown(f'<div class="{css_class}">{message["content"]}<br><span class="timestamp">{timestamp}</span></div>', unsafe_allow_html=True)

# Handle user input
if prompt := st.chat_input("Message Nexus A.I."):
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f'<div class="user-message">{prompt}<br><span class="timestamp">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span></div>', unsafe_allow_html=True)

    # Generate response
    with st.chat_message("assistant"):
        # Create a list of messages formatted for the OpenAI API
        messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        messages.append({"role": "user", "content": prompt})

        # Generate response using OpenAI
        with st.spinner("Generating response..."):
            try:
                response = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=messages,
                    temperature=0.5,
                    max_tokens=800,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                response_content = response.choices[0].message['content']
                # Display response
                st.markdown(f'<div class="assistant-message">{response_content}<br><span class="timestamp">{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</span></div>', unsafe_allow_html=True)
            except Exception as e:
                response_content = "Sorry, I couldn't generate a response."
                st.error(f"Error: {e}")

    # Append assistant message to session state
    st.session_state.messages.append({"role": "assistant", "content": response_content})

