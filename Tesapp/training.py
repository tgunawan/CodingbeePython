import tkinter as tk

window = tk.Tk()
window.title("Multiplication Table")
window.geometry("400x400")

#untuk head tabel ke bawah
for i in range(10):
  text1 = tk.Label(text = i+1 ,fg = "red")
  text1.grid(row = i+1, column = 0)
#untuk head tabel ke kanan
for i in range(10):
  text2 = tk.Label(text = i+1 ,fg = "blue")
  text2.grid(row = 0, column = i+1)
#untuk isi tabel
for i in range(10):
  for j in range(10):
    text3 = tk.Label(text = (i+1)*(j+1) ,fg = "purple")
    text3.grid(row = i+1, column = j+1)

tk.mainloop()
