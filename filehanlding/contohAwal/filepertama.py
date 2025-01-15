'''
f=open("filehanlding/contohAwal/awal.txt", "w") # membuat file , x , w 
f.write("hello world, Selamat Sore")
f.close()
f=open("filehanlding/contohAwal/awal.txt", "w") # membuat file , x , w 
f.write("Sampai jumpa ")
f.close()
try:
    f=open("filehanlding/contohAwal/awal2.txt", "x") # membuat file , x , w 
    f.write("Wow Error")
    f.close()
except FileExistsError:
    input("file sudah ada")
'''
# w => menulis ke file jika ada maka akan rewrite
# x => membuat file jika tidak ada,jika ada maka akan error
# r => hanya membaca file
# a => menambahkan data / text ke file

# with open("filehanlding/contohAwal/awal.txt", "a") as file:
#     # baca=file.read()
#     file.write("Harus 234")
#     # print(baca)

# with open("filehanlding/contohAwal/awal.txt", "w") as file:
#     file.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vel venenatis metus. Pellentesque ac libero id est egestas aliquet. Phasellus fermentum varius magna.' )
# 
# read => baca seluruh isi file
# readline => baca satu baris
# readlines => baca semua @baris dan menjadi list
# 
# 

with open("filehanlding/contohAwal/awal.txt", "r") as file:
    isi=file.readlines()
    # nama="Tedi     Gunawan "
    # print(nama.strip())
    print(isi)
print("#"*50)

for baris in isi:
    print(baris.strip(), end="")

print("#"*50)

for baris in isi: 
    print(baris.split(", "))