import sqlite3
import datetime

def log_action(user_id, action, task_id=None):
    conn = sqlite3.connect("app_kanban.db")
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().isoformat(" ", "seconds")
    cursor.execute(
        "INSERT INTO history (user_id, action, task_id, timestamp) VALUES (?, ?, ?, ?)",
        (user_id, action, task_id, timestamp)
    )
    conn.commit()
    conn.close()
