import tkinter as tk
from tkinter import messagebox
import sqlite3
from backup_utils import backup_task
from DragLabel import DragLabel
from hystory_utils import log_action


class BoardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#F9FAFB")  # Fond clair style Tailwind
        self.controller = controller
        # En haut de __init__, après self.controller = controller
        self.user_info_label = tk.Label(self, text="", font=("Arial", 12), bg="#F9FAFB", fg="#111827")
        self.user_info_label.pack(pady=10)

        self.drag_labels = []

        # Configuration responsive des colonnes
        self.column_frames = {}
        self.create_columns()
        #label d'accueil personnalisé
        self.welcome_label = tk.Label(
            self,
            text="",  # le texte sera défini dynamiquement
            font=("Arial", 12, "bold"),
            bg="#F9FAFB",
            fg="#1F2937"
        )
        self.welcome_label.pack(pady=10)


        # Bouton Nouvelle Tâche
        self.new_task_button = tk.Button(
            self,
            text="➕ Nouvelle tâche",
            command=self.open_new_task_window,
            bg="#3B82F6",
            fg="white",
            font=("Arial", 12, "bold"),
            relief="flat",
            padx=10,
            pady=5
        )
        self.new_task_button.pack(pady=10, anchor="center")
        #un bouton pour accéder à la page historique
        self.history_button = tk.Button(
            self,
            text="Voir historique des modifications",
            command=lambda: self.controller.show_frame("BackupPage"),
            bg="#6B7280",
            fg="white",
            font=("Arial", 12),
            relief="flat",
            padx=10,
            pady=5
        )
        self.history_button.pack(pady=5, anchor="center")
        #un bouton de déconnexion avec une icône
        self.logout_button = tk.Button(
            self,
            text="🚪 Se déconnecter",
            command=self.logout,
            bg="#EF4444",
            fg="white",
            font=("Arial", 12),
            relief="flat",
            padx=10,
            pady=5
        )
        self.logout_button.pack(pady=5, anchor="center")

        #un bouton de  déconnexion
        self.logout_button = tk.Button(
            self,
            text="Déconnexion",
            command=self.logout,
            bg="#EF4444",
            fg="white",
            font=("Arial", 12),
            relief="flat",
            padx=10,
            pady=5
        )
        self.logout_button.pack(pady=5, anchor="center")



        # Recharge les tâches quand visible
        self.bind("<Visibility>", lambda e: [self.load_user_info(), self.load_tasks()])

        # Responsive
        self.bind("<Configure>", self.responsive_columns)

    def create_columns(self):
        statuses = [("todo", "📝 À faire", "#FEE2E2"),
                    ("doing", "🚧 En cours", "#FEF9C3"),
                    ("done", "✅ Fini", "#D1FAE5")]

        for status, label, color in statuses:
            frame = tk.Frame(self, bg=color, relief="ridge", borderwidth=5)
            title = tk.Label(
                frame, text=label,
                font=("Arial", 14, "bold"), bg=color
            )
            title.pack(pady=10)
            self.column_frames[status] = frame
            frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def responsive_columns(self, event=None):
        width = self.winfo_width()
        side = tk.LEFT if width > 600 else tk.TOP
        for frame in self.column_frames.values():
            frame.pack_forget()
            frame.pack(side=side, fill=tk.BOTH, expand=True, padx=5, pady=5)

    def load_tasks(self):
        for frame in self.column_frames.values():
            for widget in frame.winfo_children():
                if isinstance(widget, DragLabel):
                    widget.destroy()
        self.drag_labels.clear()
        self.update_user_info()


        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, description, status FROM tasks WHERE user_id=?", (self.controller.current_user_id,))
        tasks = cursor.fetchall()
        conn.close()

        for task_id, title, description, status in tasks:
            self.create_task_label(task_id, title, description, status)

    def update_user_info(self):
        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute("SELECT email, last_connection FROM users WHERE id=?", (self.controller.current_user_id,))
        result = cursor.fetchone()
        conn.close()

        if result:
            email, last_conn = result
            self.user_info_label.config(
                text=f"Connecté en tant que : {email}\nDernière connexion : {last_conn}"
            )


    def create_task_label(self, task_id, title, description, status):
        label = DragLabel(
            parent=self.column_frames[status],
            task_id=task_id,
            title=title,
            status=status,
            user_id=self.controller.current_user_id,
            on_drop_callback=self.on_task_drop,
            text=f"{title}\n{description}",
            bg="white",  # <- COULEUR DE FOND DE LA TÂCHE
            fg="#374151",  # <- COULEUR DU TEXTE
            font=("Arial", 11),
            bd=1,
            relief="solid",
            padx=10,
            pady=5,
            justify="left"
        )
        # Attribut personnalisé ajouté après création
        label.description = description

        label.pack(pady=5, padx=10, fill="x")
        self.drag_labels.append(label)


    def open_new_task_window(self):
        new_task_win = tk.Toplevel(self)
        new_task_win.title("Ajouter une nouvelle tâche")
        new_task_win.configure(bg="#F9FAFB")

        tk.Label(new_task_win, text="Titre de la tâche :", bg="#F9FAFB", font=("Arial", 12)).pack(pady=5)
        entry_title = tk.Entry(new_task_win, font=("Arial", 12), width=30)
        entry_title.pack(pady=5)

        tk.Label(new_task_win, text="Description :", bg="#F9FAFB", font=("Arial", 12)).pack(pady=5)
        entry_description = tk.Text(new_task_win, font=("Arial", 12), height=5, width=30)
        entry_description.pack(pady=5)

        tk.Button(
            new_task_win,
            text="Ajouter",
            command=lambda: self.add_task(entry_title, entry_description, new_task_win),
            bg="#10B981",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=10,
            pady=5
        ).pack(pady=10)

    def add_task(self, entry_title, entry_description, window):
        title = entry_title.get().strip()
        description = entry_description.get("1.0", tk.END).strip()
        if not title:
            messagebox.showerror("Erreur", "Veuillez entrer un titre.")
            return
        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description, status, user_id) VALUES (?, ?,?,?)",
                       (title, description,'todo', self.controller.current_user_id))
        conn.commit()
        new_task_id = cursor.lastrowid
        log_action(self.controller.current_user_id, f"Création de la tâche '{title}'", task_id=new_task_id)
        conn.close()
        window.destroy()
        self.load_tasks()

    def on_task_drop(self, task_id, x_root, y_root):
        for status, frame in self.column_frames.items():
            x, y, w, h = frame.winfo_rootx(), frame.winfo_rooty(), frame.winfo_width(), frame.winfo_height()
            if x < x_root < x + w and y < y_root < y + h:
                conn = sqlite3.connect("app_kanban.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE tasks SET status=? WHERE id=?", (status, task_id))
                conn.commit()
                conn.close()
                self.load_tasks()
                return
        self.load_tasks()

    def update_task(self, task_id, new_title, new_description, new_status):
        # Sauvegarde avant modification
        backup_task(task_id, "modification", self.controller.current_user_id)
        log_action(self.controller.current_user_id, f"Suppression de la tâche", task_id=task_id)


        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tasks
            SET title=?, description=?, status=?
            WHERE id=?
        ''', (new_title, new_description, new_status, task_id))
        conn.commit()
        conn.close()
        self.load_tasks()

    def delete_task(self, task_id):
        # Sauvegarde avant suppression
        backup_task(task_id, "suppression", self.controller.current_user_id)

        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        conn.close()
        self.load_tasks()

    def logout(self):
        import datetime
        now = datetime.datetime.now().isoformat(" ", "seconds")
        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET last_connection=? WHERE id=?", (now, self.controller.current_user_id))
        conn.commit()
        conn.close()

        self.controller.current_user_id = None
        self.controller.show_frame("LoginPage")

    # def load_user_info(self):
        # Connexion à la base de données
    def load_user_info(self):
        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute("SELECT email, last_connection FROM users WHERE id=?", (self.controller.current_user_id,))
        user = cursor.fetchone()
        conn.close()

        if user:
            email, last_conn = user
            last_conn = last_conn if last_conn else "Jamais"
            self.welcome_label.config(text=f"👋 Bonjour {email} | Dernière connexion : {last_conn}")


