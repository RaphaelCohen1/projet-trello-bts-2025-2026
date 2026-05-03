import sqlite3

conn = sqlite3.connect("app_kanban.db")
cursor = conn.cursor()

cursor.execute("SELECT id, email, password FROM users")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Email: {row[1]}, Mot de passe: {row[2]}")

conn.close()
