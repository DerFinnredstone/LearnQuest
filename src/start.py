import tkinter as tk
from lib import start_command

root = tk.Tk()

# Erstellen einer Schaltfläche
button_start = tk.Button(root, text="Start System", command=start_command)
button_start.pack()

root.mainloop()
