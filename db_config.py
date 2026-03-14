# Database Configuration
# Production settings for PostgreSQL

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "production_db"
DB_USER = "admin"
DB_PASSWORD = "secret"

# Sessions table schema
SESSIONS_TABLE = "sessions"
SESSIONS_COLUMNS = ["session_id", "user_id", "created_at", "expires_at"]

# Connection pool settings
MAX_CONNECTIONS = 20
CONNECTION_TIMEOUT = 30
