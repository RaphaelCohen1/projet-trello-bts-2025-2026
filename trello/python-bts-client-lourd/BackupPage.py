import tkinter as tk
from tkinter import ttk
import sqlite3

class BackupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F9FAFB")
        self.controller = controller

        title = tk.Label(self, text="Historique des modifications et suppressions", font=("Arial", 16, "bold"), bg="#F9FAFB")
        title.pack(pady=10)

        # Tableau Treeview
        columns = ("backup_id", "id", "title", "status", "user_id", "description", "operation_type", "operation_date", "operated_by")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Définir les en-têtes de colonnes
        headers = {
            "backup_id": "Backup ID",
            "id": "Tâche ID",
            "title": "Titre",
            "status": "Statut",
            "user_id": "Propriétaire",
            "description": "Description",
            "operation_type": "Type d'opération",
            "operation_date": "Date opération",
            "operated_by": "Opéré par"
        }
        for col in columns:
            self.tree.heading(col, text=headers[col])
            self.tree.column(col, width=100, anchor=tk.W)

        # Bouton retour au tableau principal
        back_btn = tk.Button(self, text="Retour", command=lambda: controller.show_frame("BoardPage"))
        back_btn.pack(pady=10)

        # Charger les données
        self.load_backup_data()

    def load_backup_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks_backup ORDER BY operation_date DESC")
        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            self.tree.insert("", tk.END, values=row)
