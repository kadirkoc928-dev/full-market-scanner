import sqlite3
import time

DB = "cache.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS stock_cache (
            symbol TEXT PRIMARY KEY,
            score REAL,
            data TEXT,
            timestamp REAL
        )
    """)
    conn.commit()
    conn.close()

def get_cache(symbol, max_age=3600):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT score, data, timestamp FROM stock_cache WHERE symbol=?", (symbol,))
    row = c.fetchone()
    conn.close()

    if not row:
        return None

    score, data, ts = row
    if time.time() - ts > max_age:
        return None

    return score, data

def set_cache(symbol, score, data):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO stock_cache VALUES (?,?,?,?)
    """, (symbol, score, data, time.time()))
    conn.commit()
    conn.close()
