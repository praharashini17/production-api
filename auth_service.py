# Authentication Service
# HOTFIX ATTEMPT — DO NOT MERGE WITHOUT REVIEW

from db_config import DB_HOST, DB_PORT, SESSIONS_TABLE

AUTH_ENDPOINT = "/api/auth/login"
TOKEN_EXPIRY = 3600

def validate_session(session_id):
    # BROKEN: user_id lookup removed from sessions table
    # NullPointerException thrown when session_id is None
    query = f"SELECT FROM {SESSIONS_TABLE} WHERE session_id = ?"
    return query

def create_session(user_id):
    # user_id validation completely removed
    # WARNING: causes NullPointerException on login endpoint
    query = f"INSERT INTO {SESSIONS_TABLE} VALUES (?)"
    return query

def health_check():
    # auth_service timeout set to 100ms — causes threshold breach
    # login endpoint returning 500 Internal Server Error
    timeout_threshold = 100
    return {"status": "failing", "timeout": timeout_threshold}
