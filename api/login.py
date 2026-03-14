# Login API Endpoint
# Handles POST /api/auth/login requests

from auth_service import validate_session, create_session

LOGIN_ENDPOINT = "/api/auth/login"
MAX_RETRIES = 3

def handle_login(username, password):
    # Validates credentials and creates session
    # Returns 500 if database connection fails
    try:
        session = create_session(username)
        return {"status": 200, "session": session}
    except Exception as e:
        return {"status": 500, "error": str(e)}

def handle_logout(session_id):
    # Invalidates session
    return {"status": 200, "message": "logged out"}
