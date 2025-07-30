import streamlit as st
import requests
import json

# --- Page Configuration ---
st.set_page_config(
    page_title="Tune Buddy",
    page_icon="🎵",
    layout="centered"
)

# --- Dify API Communication ---
# This function calls the Dify API using the secret key
def get_tune_buddy_recommendation(user_query):
    # Retrieve API key and URL from secrets
    api_key = st.secrets.get("DIFY_API_KEY")
    api_url = st.secrets.get("DIFY_API_URL")

    if not api_key or not api_url:
        st.error("API Key or URL not found. Please check your secrets.toml file.")
        return "API configuration error."

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        "inputs": {},
        "query": user_query,
        "user": "streamlit-user-123", # A unique ID for the end-user
        "response_mode": "blocking"
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        api_response = response.json()
        return api_response.get('answer', "Sorry, I couldn't get a recommendation right now.")
    except requests.exceptions.RequestException as e:
        st.error(f"API Request Error: {e}")
        return "Sorry, there was an issue connecting to the service."

# --- Streamlit App UI ---
st.title("🎵 Tune Buddy")
st.markdown("Your personal AI music companion. Tell me your mood, a genre, or an artist, and I'll find the perfect tune for you!")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What kind of music are you in the mood for?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Finding the perfect tune..."):
            response = get_tune_buddy_recommendation(prompt)
            st.markdown(response)
    # Add AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})