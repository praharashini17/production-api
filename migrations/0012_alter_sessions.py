# Migration 0012 — Alter Sessions Table
# Adds user_id column to sessions table

MIGRATION_ID = "0012"
MIGRATION_NAME = "alter_sessions_add_user_id"

def up():
    # Apply migration
    sql = """
    ALTER TABLE sessions 
    ADD COLUMN user_id INTEGER;
    
    CREATE INDEX idx_sessions_user_id 
    ON sessions(user_id);
    """
    return sql

def down():
    # Rollback migration
    sql = """
    ALTER TABLE sessions 
    DROP COLUMN user_id;
    """
    return sql
