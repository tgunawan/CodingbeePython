import os
# 1st object
os.system('cls')

class Hewan:
    def __init__(self, nama):
        self.nama = nama
    def suara(self):
        print("Suara Hewan")

class Kucing(Hewan):
    def __init__(self, nama,warna):
        super().__init__(nama)
        self.warna = warna

    def suara(self):
        print("Meow",self.nama)

class Anjing(Hewan):
    def __init__(self, nama,ras):
        super().__init__(nama)
        self.ras = ras
    def suara(self):
        print("Guk guk")


anjing=Anjing("Doggy","Hachiko")
kucing=Kucing("Shiro","Putih")

anjing.suara()
kucing.suara()





'''
class Hewan:
    def suara(self):
        print("Suara Hewan")

class Kucing():
    def suara(self):
        print("Meow")

class Anjing():
    def suara(self):
        print("Guk guk")


anjing=Anjing()
kucing=Kucing()

anjing.suara()
kucing.suara()

# 2 inheritance


class bentuk:
    def luas(self):
        pass

class persegi(bentuk):
    def __init__(self,sisi):
        self.sisi=sisi
    def luas(self):
        return self.sisi*self.sisi

class lingkaran(bentuk):
    def __init__(self,radius):
        self.radius=radius
    def luas(self):
        return 3.14*self.radius*self.radius

class segitiga(bentuk):
    def __init__(self, alas, tinggi):
        self.alas=alas
        self.tinggi=tinggi

    def luas(self):
        return 0.5*self.alas*self.tinggi



bentuk1=persegi(5)
bentuk2=lingkaran(10)
bentuk3=segitiga(10,20)

print("Luas persegi:",bentuk1.luas())
print("Luas lingkaran:",bentuk2.luas())
print('Luas segitiga: ', bentuk3.luas())





class Part:
    def Block(self):
        print("This is a block") 


print(Part.Block('cylinder'))

part=Part()
print(part)'''