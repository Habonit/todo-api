import sqlite3
from typing import Optional

_conn: Optional[sqlite3.Connection] = None


def init_db(path: str = "todos.db") -> None:
    global _conn
    _conn = sqlite3.connect(path, check_same_thread=False)
    _conn.row_factory = sqlite3.Row
    _conn.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            title     TEXT    NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)
    _conn.commit()


def get_conn() -> sqlite3.Connection:
    if _conn is None:
        raise RuntimeError("Database not initialised")
    return _conn


def close_db() -> None:
    global _conn
    if _conn is not None:
        _conn.close()
        _conn = None
