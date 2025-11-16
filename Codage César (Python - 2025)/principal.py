import tkinter as tk
from tkinter import messagebox
import decodage

def encoder():
    clef = input_number.get()  # Récupérer la clef de l'utilisateur
    message_code = text_area.get("1.0", tk.END).strip()  # Récupérer le texte de l'utilisateur
    resultat = decodage.try_except_decodage(message_code, clef)
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", resultat)

def tout_tester():
    resultat = decodage.tout_tester(text_area.get("1.0", tk.END).strip())
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", resultat)

# Création de la fenêtre principale
root = tk.Tk() 
root.title("Codage César")
root.geometry("300x250")

# Création d'un label
label = tk.Label(root, text="Entrez un message et une clef.", font=("Arial", 12))
label.pack(pady=10)

# Création d'une zone de texte
text_area = tk.Text(root, height=5, width=30)
text_area.pack(pady=10)

# Création d'une frame pour aligner les éléments
frame = tk.Frame(root)
frame.pack(pady=10)

# Création d'une case de texte pour l'entrée de l'utilisateur
input_number = tk.Entry(frame, width=20)
input_number.pack(side=tk.LEFT)

# Création d'un bouton
button = tk.Button(frame, text="Encoder / Décoder", command=encoder)
button.pack(side=tk.LEFT)

# Création d'un bouton
button2 = tk.Button(root, text="Tout essayer", command=tout_tester)
button2.pack(pady=10)

# Lancer la boucle principale
root.mainloop()
