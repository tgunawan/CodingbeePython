import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Testing Pack Area")
window.geometry("500x300")

#Area Notebook
note=ttk.Notebook(window)
note.pack(fill="both",expand=True)

#Tab pertama
tab1=ttk.Frame(note)
note.add(tab1, text="Tab pertama coba")

#Tab kedua
tab2=ttk.Frame(note)
note.add(tab2, text="Tab kedua coba")

textLabel1 = tk.Label(tab1,text="Tab Pertama bagian isi")
textLabel1.pack(pady=20)


textLabel2 = tk.Label(tab2,text="Tab kedua1 bagian isi")
textLabel2.pack(pady=20,side=tk.BOTTOM)
textLabel2 = tk.Label(tab2,text="Tab kedua2 bagian isi")
textLabel2.pack(pady=20, side=tk.LEFT)
textLabel2 = tk.Label(tab2,text="Tab kedua3 bagian isi")
textLabel2.pack(pady=20, side=tk.RIGHT)



window.mainloop()