import tkinter as tk
from tkinter import ttk

# Tkinter Objekt in Variable "root" instanziieren
root = tk.Tk()
# Beschreibendes Label
lbl_instruction = ttk.Label(root, text="Bitte Text eingeben:")
lbl_instruction.grid(column=0, row=0, padx=10, pady=5)
# Inputfeld
inp_entry = ttk.Entry(root)
inp_entry.grid(column=0, row=1, padx=10, pady=10)
# Funktion, die bei Klick auf Button aufgerufen wird
def submit():
    x = inp_entry.get()
    lbl_out = ttk.Label(root, text=x, foreground="blue")
    lbl_out.grid(column=0, row=3, padx=10, pady=15)
# Button, der Funktion "submit" aufruft
btn_submit = ttk.Button(root, text="Senden", command=submit)
btn_submit.grid(column=0, row=2, padx=10, pady=5, sticky='nesw')
# Eventschleife starten: Methode wartet auf Ereignisse, wie das Klicken eines Buttons
root.mainloop()