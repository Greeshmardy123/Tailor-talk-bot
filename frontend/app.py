import streamlit as st
import requests

st.title("TailorTalk1: AI Appointment Booking")

backend_url = st.secrets.get("backend_url", "http://localhost:8000/chat")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("You:", "")
if st.button("Send") and user_input:
    st.session_state["messages"].append(("You", user_input))
    try:
        response = requests.post(backend_url, json={"message": user_input})
        bot_reply = response.json().get("message", "(No response)")
    except Exception as e:
        bot_reply = f"Error: {e}"
    st.session_state["messages"].append(("Bot", bot_reply))

for sender, msg in st.session_state["messages"]:
    st.write(f"**{sender}:** {msg}") 