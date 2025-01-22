import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Testing Pack Area")
window.geometry("500x300")

note=ttk.Notebook(window)
note.pack(fill="both",expand=True)

window.mainloop()