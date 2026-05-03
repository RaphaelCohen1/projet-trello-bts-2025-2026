import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import BoardPage
import LoginPage
import BackupPage

# ============= CREATION DE LA BD ET DES TABLES ============= #

conn = sqlite3.connect("app_kanban.db")# Connexion à la base de données SQLite qui est nommée "app_kanban.db".SQILite est un système de gestion de base de données relationnelle léger et intégré.
cursor = conn.cursor()

# Table des utilisateurs
cursor.execute('''\
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    last_connection TEXT,
    password TEXT NOT NULL
)''')
# Ajoute la colonne last_connection si elle n'existe pas déjà
try:
    cursor.execute("ALTER TABLE users ADD COLUMN last_connection TEXT")
except sqlite3.OperationalError:
    pass  # Ignore si elle existe déjà

# Table de l'historique des actions
# Cette table enregistre les actions des utilisateurs, comme la création de tâches, les modifications,
cursor.execute('''
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    action TEXT NOT NULL,
    task_id INTEGER,
    timestamp TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(task_id) REFERENCES tasks(id)
)
''')

#crée une table tasks_backup qui contient toutes les colonnes de tasks + des colonnes supplémentaires pour tracer
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks_backup (
    backup_id INTEGER PRIMARY KEY AUTOINCREMENT,
    id INTEGER,  -- id d'origine dans tasks
    title TEXT,
    status TEXT,
    user_id INTEGER,
    description TEXT,
    operation_type TEXT NOT NULL,  -- 'modification' ou 'suppression'
    operation_date TEXT NOT NULL,
    operated_by INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(operated_by) REFERENCES users(id)
)
''')


# Table des taches
cursor.execute('''\
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    status TEXT NOT NULL,  -- 'todo', 'doing', 'done'
    user_id INTEGER,
    description TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)''')

conn.commit()
conn.close()

# =============================================== #

class KanbanApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application Kanban - BTS SIO SLAM")
        self.geometry("800x600")

        # Conteneur de pages (frames)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage.LoginPage, BoardPage.BoardPage, BackupPage.BackupPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")
        self.current_user_id = None

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def set_current_user(self, user_id):
        self.current_user_id = user_id




if __name__ == "__main__":
    app = KanbanApp()
    app.mainloop()