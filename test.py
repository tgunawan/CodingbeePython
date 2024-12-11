import os

angka=0
mulai1=0
mulai2=0

while True:
    os.system('cls')
    try:
        angka = int(input("Masukkan angka: "))
    except:
        input("Masukkan angka\nTekan enter untuk mengulang")
        continue
    else:
        if angka == 1:
            if mulai1 == 0:
                mulai1 = 1
                input("Putih")
            else:
                mulai1 = 0
                input("Kuning")
        elif angka == 0:
            if mulai2 == 0:
                mulai2 = 1
                input("Putih")
            else:
                mulai2 = 0
                input("Kuning")
        else:
            input("Masukkan angka 1 atau 0\nTekan enter untuk mengulang")