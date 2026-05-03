import tkinter as tk #Importe Tkinter sous l'alias tk pour créer l'interface graphique.
from tkinter import ttk, messagebox# Importe les modules ttk pour des widgets améliorés et messagebox pour les boîtes de dialogue.
import sqlite3#Importe SQLite pour la gestion de la base de données.
import datetime#Importe le module datetime pour gérer les dates et heures.
from hystory_utils import log_action# Importe la fonction log_action pour enregistrer les actions des utilisateurs.



class LoginPage(tk.Frame):# Page de connexion héritant de tk.Frame.
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Frame centrale, avec un fond blanc et des bordures. Frame est le cadre créer dans la page de connexion.
        # Il est centré dans la fenêtre avec un rembourrage de 200 pixels à gauche et à droite, et 20 pixels en haut et en bas. 
        frame = tk.Frame(self, bg="white", padx=200, pady=20, relief="ridge", bd=2)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Titre
        tk.Label(frame, text="Connexion", font=("Arial", 16, "bold"), bg="white", fg="#111827").pack(pady=(0, 10))# tk.label permet d'afficher le titre "Connexion" en haut du formulaire de login.

        # Champ Email
        tk.Label(frame, text="Adresse e-mail", font=("Arial", 10), bg="white", fg="#6b7280").pack(anchor="w")
        self.entry_email = tk.Entry(frame, font=("Arial", 12), bg="#f9fafb", fg="#111827", relief="flat", bd=2)#self est une variable représentant le champ de saisie (input) où l'utilisateur tape son adresse e-mail.
        self.entry_email.pack(fill="x", padx=5, pady=5, ipady=5)
        
        # Champ Mot de passe
        tk.Label(frame, text="Mot de passe", font=("Arial", 10), bg="white", fg="#6b7280").pack(anchor="w")
        self.entry_password = tk.Entry(frame, font=("Arial", 12), bg="#f9fafb", fg="#111827", relief="flat", bd=2, show="*")
        self.entry_password.pack(fill="x", padx=5, pady=5, ipady=5)

        # Bouton Se connecter
        self.btn_login = tk.Button(frame, text="Se connecter", font=("Arial", 12, "bold"), bg="#3b82f6", fg="white",
            relief="flat", bd=0, activebackground="#2563eb", activeforeground="white",
            command=self.login)# self.btn_login est une variable représentant le bouton "Se connecter".
        self.btn_login.pack(fill="x", pady=10, ipady=5)

        # Bouton S'inscrire
        self.btn_register = tk.Button(frame, text="S'inscrire", font=("Arial", 12, "bold"), bg="#10b981", fg="white",
            relief="flat", bd=0, activebackground="#059669", activeforeground="white",
            command=self.register)
        self.btn_register.pack(fill="x", ipady=5)
        

    def login(self):
        print ("Login appelé")  # Pour le débogage, affiche un message dans la console.
        print("Tentative de connexion...")  # Pour le débogage, affiche un message dans la console.
        email = self.entry_email.get()
        password = self.entry_password.get()

        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            now = datetime.datetime.now().isoformat(" ", "seconds")

            # Mise à jour de la date de dernière connexion
            cursor.execute("UPDATE users SET last_login=? WHERE id=?", (now, user_id))
            conn.commit()
            conn.close()
            log_action(user_id, "Connexion")

            self.controller.set_current_user(user_id)
            self.controller.show_frame("BoardPage")
        else:
            conn.close()
            messagebox.showerror("Erreur", "Identifiants invalides.")


    def register(self):
        print("register appelé")  # Pour le débogage, affiche un message dans la console.
        email = self.entry_email.get()
        password = self.entry_password.get()
        if not email or not password:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        conn = sqlite3.connect("app_kanban.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            messagebox.showinfo("Succès", "Inscription réussie !")
        
        except sqlite3.IntegrityError:
            messagebox.showerror("Erreur", "Cet email est déjà enregistré.")
        conn.close()
