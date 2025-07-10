import sqlite3
import os
from datetime import datetime

DATABASE_PATH = "translation_logs.db"

async def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Create translation_logs table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS translation_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_text TEXT NOT NULL,
        target_language TEXT NOT NULL,
        translated_text TEXT NOT NULL,
        timestamp DATETIME NOT NULL
    )
    """)
    
    conn.commit()
    conn.close()

async def log_translation(source_text, target_language, translated_text):
    """Log a translation request to the database"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO translation_logs (source_text, target_language, translated_text, timestamp) VALUES (?, ?, ?, ?)",
        (source_text, target_language, translated_text, datetime.now().isoformat())
    )
    
    conn.commit()
    conn.close()