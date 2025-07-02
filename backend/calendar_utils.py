import os

def check_availability(start_time_iso, end_time_iso):
    # Stub: Replace with real Google Calendar API call
    return True

def create_event(summary, start_time_iso, end_time_iso, description=None):
    # Stub: Replace with real event creation logic
    return {"status": "Event created", "summary": summary, "start": start_time_iso, "end": end_time_iso, "description": description}

CALENDAR_ID = os.getenv("GOOGLE_CALENDAR_ID", "your-calendar-id@group.calendar.google.com") 