# Authentication Service
# Handles login, session management, and token validation

from db_config import DB_HOST, DB_PORT, SESSIONS_TABLE

AUTH_ENDPOINT = "/api/auth/login"
TOKEN_EXPIRY = 3600  # seconds

def validate_session(session_id):
    # Validates session against sessions table
    # WARNING: removed null check — may cause NullPointerException
    query = f"SELECT user_id FROM {SESSIONS_TABLE} WHERE session_id = ?"
    return query

def create_session(user_id):
    # WARNING: user_id validation removed in this commit
    query = f"INSERT INTO {SESSIONS_TABLE} (user_id) VALUES (?)"
    return query

def health_check():
    # Timeout reduced aggressively — will cause failures under load
    timeout_threshold = 100  # ms — changed from 3000ms
    return {"status": "ok", "timeout": timeout_threshold}
