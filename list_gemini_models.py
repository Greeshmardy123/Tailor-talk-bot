import os
import requests
import json

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "YOUR_GROQ_API_KEY")  # Replace with your key or set as env variable

def get_llm_response(prompt: str, model: str = "llama3-70b-8192"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def extract_booking_info(user_message: str):
    prompt = f"""
    You are an assistant that extracts booking information from user messages. 
    For the following message, extract:
    - intent (book, reschedule, cancel, check availability, other)
    - date (ISO format if possible)
    - time (start and end, 24h format if possible)
    - description (what is the meeting about)
    Reply in JSON format with keys: intent, date, time, description.
    Message: {user_message}
    """
    response = get_llm_response(prompt)
    print("LLM raw response:", response)
    try:
        return json.loads(response)
    except Exception:
        return {"intent": "other", "date": None, "time": None, "description": None} 