import tkinter as tk

window=tk.Tk()
window.title("Multiplication Table")
window.geometry("800x400")

title=tk.Label(text="Multiplication Table",fg="red",bg="white")
title.grid(row=0, column=0,columnspan=10)
# title=tk.Label(text="Multiplication Table kolom2",fg="red",bg="white")
# title.grid(row=0, column=1)
# space=tk.Label(text=" ",fg="red")
# space.grid(row=2, column=2)
# title=tk.Label(text="Multiplication Table baris2",fg="red",bg="white")
# title.grid(row=3, column=3)

for i in range(1,11):
    headercolumn=tk.Label(window,text=i,font=("Arial",10,"bold"),fg="orange")
    headercolumn.grid(row=1,column=i)

for i in range(2,12):
    headerrow=tk.Label(window,text=i-1,font=("Arial",10,"bold"),fg="orange")
    headerrow.grid(row=i,column=0)

for i in range(2,12):
    for j in range(1,11):
        result=(i-1)*j
        labelhasil=tk.Label(window,text=result)
        labelhasil.grid(row=i,column=j)

        
window.mainloop()