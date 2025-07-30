
# 🎵 Tune Buddy - AI Music Companion

Welcome to **Tune Buddy**, your personal **AI-powered music companion**! This interactive web application recommends **Telugu songs** based on your mood, favorite genres, or artists—and can even **compose a brand-new, original song just for you**!

🌐 **[Live App Demo](https://tune-buddy.streamlit.app/)**

---

## ✨ Key Features

- **🎙 Conversational Recommendations**  
  Chat naturally with the AI to get song suggestions tailored to your mood or music taste.

- **📝 AI Songwriter**  
  Ask the assistant to "create a song"—it will generate original lyrics based on your given theme.

- **📚 Persistent Chat History**  
  All your conversations are saved. Revisit previous chats and recommendations from the sidebar.

- **🆕 New Chat Functionality**  
  Start a fresh session anytime with the “New Chat” button.

- **💻 Interactive Frontend**  
  A clean, responsive, and user-friendly interface built using Streamlit.

---

## 🛠️ Tech Stack

This project demonstrates a complete full-stack development cycle, from AI backend integration to frontend deployment and persistent storage.

| Layer        | Technology Used                        |
|-----------------|----------------------------------------|
| **AI Backend** | [Dify.ai](https://dify.ai) with LLMs like ChatGPT or Gemini |
| **Frontend**  | [Streamlit](https://streamlit.io) (Python) |
| **Database**  | [Google Firestore](https://firebase.google.com/docs/firestore) |
| **Deployment**| [Streamlit Community Cloud](https://streamlit.io/cloud) |
| **Version Control** | Git & GitHub |

---

## ⚙️ How to Run Locally

Follow these steps to set up the project on your machine:

### 1. Clone the Repository

```bash
git clone https://github.com/Umarfaaruk/Tune-Buddy-app.git
cd Tune-Buddy-app
````

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv
# For Windows
.\venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Secrets

Create a file named `.streamlit/secrets.toml` and add your credentials:

```toml
# .streamlit/secrets.toml
[dify]
api_key = "your_dify_api_key"
base_url = "your_dify_base_url"

[firebase]
type = "service_account"
project_id = "your_project_id"
private_key_id = "your_private_key_id"
private_key = "your_private_key"
client_email = "your_client_email"
client_id = "your_client_id"
# ... rest of your Firebase service account fields
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 🤝 Contributions

Feel free to fork this repository, submit pull requests, or open issues if you’d like to contribute to Tune Buddy!

---

## 👨‍💻 Developed By

**Umar Faaruk**

> Built with ❤️ to blend AI and culture through music!

```
