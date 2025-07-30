import streamlit as st
import requests
import json
import uuid # To generate unique IDs for chat sessions
from google.cloud import firestore
from google.oauth2 import service_account

# --- Firestore Connection ---

def get_firestore_client():
    """
    Connects to Firestore using credentials stored in Streamlit's secrets.
    """
    try:
        # Get the service account key from secrets
        key_dict = json.loads(st.secrets["firestore_key"])
        creds = service_account.Credentials.from_service_account_info(key_dict)
        db = firestore.Client(credentials=creds)
        return db
    except Exception as e:
        st.error(f"Firestore connection failed: {e}")
        return None

# --- Dify API Communication ---

def get_tune_buddy_recommendation(user_query, conversation_id):
    """
    Calls the Dify API to get a music recommendation.
    """
    api_key = st.secrets.get("DIFY_API_KEY")
    api_url = st.secrets.get("DIFY_API_URL")

    if not api_key or not api_url:
        st.error("API Key or URL not found. Please check your secrets.")
        return "API configuration error."

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        "inputs": {},
        "query": user_query,
        "user": "streamlit-user-123",
        "conversation_id": conversation_id, # Pass conversation_id to Dify
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

# --- Main App UI ---

st.set_page_config(page_title="Tune Buddy", page_icon="🎵", layout="centered")

db = get_firestore_client()

# --- Sidebar for Chat History ---

st.sidebar.title("Chat History")

if st.sidebar.button("➕ New Chat"):
    st.session_state.chat_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.rerun()

# Fetch and display previous chat sessions
if db:
    chats_ref = db.collection("chats").stream()
    chat_ids = [chat.id for chat in chats_ref]
    for chat_id in chat_ids:
        # Use a descriptive name for the button, like the first user message
        try:
            first_message = db.collection("chats").document(chat_id).collection("messages").document("message_0").get()
            button_label = first_message.to_dict().get('content', 'Chat')[:30] + "..."
        except:
            button_label = chat_id[:8] # Fallback to short ID

        if st.sidebar.button(button_label, key=chat_id):
            st.session_state.chat_id = chat_id
            # Load messages for the selected chat
            messages_ref = db.collection("chats").document(chat_id).collection("messages").order_by("timestamp").stream()
            st.session_state.messages = [msg.to_dict() for msg in messages_ref]
            st.rerun()


# --- Chat Interface ---

st.title("🎵 Tune Buddy")
st.markdown("Your personal AI music companion. Tell me your mood, a genre, or an artist, and I'll find the perfect tune for you!")


# Initialize session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_id" not in st.session_state:
    st.session_state.chat_id = str(uuid.uuid4())


# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What kind of music are you in the mood for?"):
    # Add user message to chat history and display it
    user_message = {"role": "user", "content": prompt, "timestamp": firestore.SERVER_TIMESTAMP}
    st.session_state.messages.append(user_message)
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Save user message to Firestore
    if db:
        msg_ref = db.collection("chats").document(st.session_state.chat_id).collection("messages")
        msg_ref.document(f"message_{len(st.session_state.messages)-1}").set(user_message)


    # Get and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Finding the perfect tune..."):
            # Pass the existing chat_id to Dify to maintain context
            dify_conversation_id = st.session_state.get('dify_conversation_id', None)
            response_text = get_tune_buddy_recommendation(prompt, dify_conversation_id)
            st.markdown(response_text)
    
    # Add AI response to chat history and save to Firestore
    assistant_message = {"role": "assistant", "content": response_text, "timestamp": firestore.SERVER_TIMESTAMP}
    st.session_state.messages.append(assistant_message)
    if db:
        msg_ref = db.collection("chats").document(st.session_state.chat_id).collection("messages")
        msg_ref.document(f"message_{len(st.session_state.messages)-1}").set(assistant_message)

