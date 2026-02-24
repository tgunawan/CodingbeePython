'''tk.StringVar(): Ini adalah variabel khusus Tkinter yang menampung nilai dari Radio Button yang sedang dipilih.

variable=var_ops: Menghubungkan semua Radio Button ke satu grup yang sama sehingga hanya satu yang bisa dipilih dalam satu waktu.

try...except: Digunakan untuk mencegah program crash jika pengguna memasukkan teks (bukan angka) atau mengosongkan kolom.

anchor="w": Menjaga agar pilihan Radio Button rata kiri agar terlihat lebih rapi.'''

import tkinter as tk
from tkinter import messagebox

def hitung():
    try:
        # Mengambil angka dari entry
        num1 = float(entry_1.get())
        num2 = float(entry_2.get())
        operasi = var_ops.get()
        
        # Logika perhitungan berdasarkan radio button
        if operasi == "Tambah":
            hasil = num1 + num2
        elif operasi == "Kurang":
            hasil = num1 - num2
        elif operasi == "Kali":
            hasil = num1 * num2
        elif operasi == "Bagi":
            if num2 == 0:
                messagebox.showerror("Error", "Tidak bisa membagi dengan nol!")
                return
            hasil = num1 / num2
        else:
            messagebox.showwarning("Peringatan", "Pilih operasi terlebih dahulu!")
            return

        label_hasil.config(text=f"Hasil: {hasil}")
        
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Inisialisasi Window
root = tk.Tk()
root.title("Kalkulator Radio Button")
root.geometry("300x400")

# Input Angka
tk.Label(root, text="Angka Pertama:").pack(pady=5)
entry_1 = tk.Entry(root)
entry_1.pack()

tk.Label(root, text="Angka Kedua:").pack(pady=5)
entry_2 = tk.Entry(root)
entry_2.pack()

# Radio Button Operasi
tk.Label(root, text="\nPilih Operasi:", font=('Arial', 10, 'bold')).pack()

var_ops = tk.StringVar(value="Tambah") # Default value

opsi = ["Tambah", "Kurang", "Kali", "Bagi"]
for teks in opsi:
    tk.Radiobutton(root, text=teks, variable=var_ops, value=teks).pack(anchor="w", padx=100)

# Tombol Hitung
btn_hitung = tk.Button(root, text="HITUNG", command=hitung, bg="#4CAF50", fg="white")
btn_hitung.pack(pady=20)

# Label Hasil
label_hasil = tk.Label(root, text="Hasil: -", font=('Arial', 12, 'bold'))
label_hasil.pack()

root.mainloop()