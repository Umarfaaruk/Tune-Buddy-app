🎵 Tune Buddy - AI Music Companion
Welcome to Tune Buddy, your personal AI-powered music companion! This interactive web application recommends Telugu songs based on your mood, favorite genres, or artists. But it doesn't stop there—it can even compose a brand new, original song just for you!

🚀 Check out the live app here:
           https://tune-buddy.streamlit.app/

✨ Key Features
Conversational Recommendations: Chat naturally with the AI to get song suggestions tailored to your mood or taste.

AI Songwriter: Ask the assistant to "create a song," and it will generate original lyrics based on your theme.

Persistent Chat History: All your conversations are saved! You can revisit previous chats and recommendations from the sidebar.

New Chat Functionality: Easily start a fresh conversation at any time with the "New Chat" button.

Interactive Frontend: A clean, responsive, and user-friendly interface built with Streamlit.

🛠️ Tech Stack
This project demonstrates a full-stack development cycle, from the AI backend to a deployed frontend with a persistent database.

AI Backend: Dify.ai for orchestrating the LLM (like Gemini or ChatGPT) and managing the prompt engineering.

Frontend: Streamlit for building the interactive web application in Python.

Database: Google Firestore for storing and retrieving chat histories, enabling persistent conversations.

Deployment: Streamlit Community Cloud for hosting the live application.

Version Control: Git & GitHub for source code management.

⚙️ How to Run Locally
To run this project on your own machine, follow these steps:

Clone the repository:

git clone https://github.com/Umarfaaruk/Tune-Buddy-app.git
cd Tune-Buddy-app

Create and activate a virtual environment:

python -m venv venv
.\venv\Scripts\activate

Install the required libraries:

pip install -r requirements.txt

Set up your secrets:

Create a file at .streamlit/secrets.toml.

Add your Dify API key and URL, and your Firebase service account key (JSON).

Run the app:

streamlit run app.py
