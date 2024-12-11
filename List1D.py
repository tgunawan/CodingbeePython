#------- library-----------------
import os

#------- Variables-----------------
list=[]
list2=[]
#------- Functions-----------------
def display(list):
    os.system('cls')
    # print(list)
    # for item in list:
    #     print(item,end=" ")
    for i in range(len(list)):
        print(f'{i+1}. {list[i]}')

def hapus(nama):
    list.remove(nama)
    display(list)

def delete(angka):
    list.pop(angka-1)
    display(list)

#------- Main-----------------
display(list)
list.append(3)
display(list)
list.append("Tiga")
display(list)

'''nama=int(input("Masukkan nomor yang ingin di hapus: "))
hapus(nama)
delete(nama)'''

list[0] = ""
print(list[0])
display(list)

'''ulang=int(input("Masukkan jumlah yang ingin di tambahkan: "))
for i in range(ulang):
    list2.append(input("Masukkan nama: "))'''

while "y" in input("Tambah lagi? (y/n) ").lower():
    list2.append(input("Masukkan nama: "))

list+=list2
print(list)
print(",".join(list))

#------- End Main----------------