# TailorTalk1: AI Appointment Booking

This project is an AI-powered conversational agent for booking appointments on Google Calendar. It uses FastAPI for the backend and Streamlit for the frontend.

## Features
- Conversational chat interface
- Google Calendar integration (via service account)
- LLM-powered intent extraction (stubbed for now)

## Project Structure
```
TailorTalk1/
  backend/
    main.py
    agent.py
    calendar_utils.py
    llm_utils.py
    requirements.txt
  frontend/
    app.py
    requirements.txt
  .gitignore
  README.md
```

## Setup Instructions

### 1. Backend (FastAPI)
```sh
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. Frontend (Streamlit)
```sh
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

### 3. Environment Variables
- Set `GOOGLE_CALENDAR_ID` and `GROQ_API_KEY` as environment variables for backend.
- Store your Google service account JSON securely (do not commit to git).

### 4. Deployment
- Use Railway, Render, or similar platforms for deployment.
- Store secrets using the platform's secret manager.

---

**This is a starter scaffold. Add your Google Calendar and LLM integration as needed!** 