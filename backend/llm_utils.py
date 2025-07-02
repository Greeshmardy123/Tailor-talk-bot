import os
import requests
import json
import re

# Load your LLM API key from environment variable
LLM_API_KEY = os.getenv("LLM_API_KEY")  # Set this in your deployment environment

# Choose your LLM endpoint and model
LLM_API_URL = os.getenv("LLM_API_URL", "https://api.openai.com/v1/chat/completions")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")

def get_llm_response(prompt: str, model: str = None):
    """
    Call the LLM API to get a response for the given prompt.
    """
    if model is None:
        model = LLM_MODEL
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    response = requests.post(LLM_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def extract_json_from_response(response: str):
    """
    Try to extract the first JSON object from the response string.
    """
    match = re.search(r'\{.*\}', response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except Exception:
            pass
    return None

def extract_booking_info(user_message: str):
    """
    Use the LLM to extract intent, date, time, and description from the user's message.
    Returns a dict with keys: intent, date, time, description.
    """
    prompt = f"""
You are an assistant that extracts booking information from user messages. 
For the following message, extract:
- intent (book, reschedule, cancel, check availability, other)
- date (ISO format if possible)
- time (start and end, 24h format if possible)
- description (what is the meeting about)
Reply with ONLY a valid JSON object with keys: intent, date, time, description. Do not include any explanation or text outside the JSON.
Message: {user_message}
"""
    response = get_llm_response(prompt)
    print("LLM raw response:", response)
    # Try to parse as JSON directly
    try:
        return json.loads(response)
    except Exception:
        # Try to extract JSON from the response
        extracted = extract_json_from_response(response)
        if extracted:
            return extracted
        return {"intent": "other", "date": None, "time": None, "description": None} 