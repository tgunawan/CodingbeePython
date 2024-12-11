import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

# tes comment
switch=True
window=tk.Tk()
window.title("File Explorer")
window.geometry("500x500")


'''tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)

tabControl.add(tab1, text="File Explorer")
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)

tabControl.add(tab2, text="File baru")
tabControl.pack(expand=1, fill="both")'''

def windowSwitch():
    global switch
    if switch:
        switch=False
        MainPage.pack_forget()
        SecondPage.pack(fill="both", expand=True)
    else:
        switch=True
        SecondPage.pack_forget()
        MainPage.pack(fill="both", expand=True)

MainPage=tk.Frame(window)
MainPage.pack(fill="both", expand=True)

teksJudul = tk.Label(MainPage, text="Main Page")
teksJudul.pack()

tombol_Switch=tk.Button(MainPage, text="Switch", command=windowSwitch)
tombol_Switch.pack()

SecondPage=tk.Frame(window)
SecondPage.pack(fill="both", expand=True)

teksJudul2 = tk.Label(SecondPage, text="Second Page")
teksJudul2.pack()

tombol_Switch2=tk.Button(SecondPage, text="Switch", command=windowSwitch)
tombol_Switch2.pack()

SecondPage.pack_forget()
MainPage.pack(fill="both", expand=True)

window.mainloop()