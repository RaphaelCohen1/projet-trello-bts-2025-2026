import sqlite3
import datetime

def backup_task(task_id, operation_type, operated_by):
    conn = sqlite3.connect("app_kanban.db")
    cursor = conn.cursor()

    # Récupérer la ligne avant modification ou suppression
    cursor.execute("SELECT id, title, status, user_id, description FROM tasks WHERE id=?", (task_id,))
    row = cursor.fetchone()

    if row:
        operation_date = datetime.datetime.now().isoformat(" ", "seconds")
        cursor.execute('''
            INSERT INTO tasks_backup (id, title, status, user_id, description, operation_type, operation_date, operated_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (*row, operation_type, operation_date, operated_by))
        conn.commit()

    conn.close()
