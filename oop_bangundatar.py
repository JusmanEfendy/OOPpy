print("\n===OOP BANGUNDATAR===")

class bangundatar():
    bila = None
    bilb = None
    hasil = None
    tinggi = None
    d1 = None
    d2 = None
    r = None
    bilc = None
    bild = None


    def __init__(self, bila, bilb, hasil, tinggi, d1, d2, r, bilc, bild):
        self.bila = bila
        self.bilb = bilb
        self.hasil = hasil
        self.tinggi = tinggi
        self.bilc = bilc
        self.bild = bild
        self.d1 = d1
        self.d2 = d2
        self.r = r
        

    def persegi(self):
        hasil = self.bila * 4
        print(f"Keliling Persegi = {hasil}")
        hasil = self.bila * self.bilb
        print(f"Luas Persegi = {hasil}")
        return hasil

    def persegipanjang(self):
        hasil = 2 * (self.bila + self.bilb)
        print(f"Keliling Persegi Panjang = {hasil}")
        hasil = self.bila * self.bilb
        print(f"Luas Persegi Panjang = {hasil}")
        return hasil

    def jajargenjang(self):
        hasil = 2 * (self.bila + self.bilb)
        print(f"Keliling Jajar Genjang = {hasil}")
        hasil = self.bila * self.tinggi 
        print(f"Luas Jajar Genjang = {hasil}")
        return hasil

    def segitiga(self):
        hasil = self.bila + self.bilb + self.bilc
        print(f"Keliling Segitiga = {hasil}")
        hasil = (self.bilb * self.tinggi) * 0.5
        print(f"Luas Segitiga = {hasil}")
        return hasil

    def belahketupat(self):
        hasil = self.bila + self.bilb + self.bilc + self.bild
        print(f"Keliling Belah Ketupat = {hasil}")
        hasil = 0.5 * (self.d1 * self.d2)
        print(f"Luas Belah Ketupat = {hasil}")
        return hasil

    def layanglayang(self):
        hasil = self.bila + self.bilb + self.bilc + self.bild
        print(f"Keliling Layang-layang = {hasil}")
        hasil = 0.5 * (self.d1 * self.d2)
        print(f"Luas Layang-layang = {hasil}")
        return hasil
    
    def trapesium(self):
        hasil = self.bila + self.bilb + self.bilc + self.bild
        print(f"Keliling Trapesium = {hasil}")
        hasil = ((self.bila + self.bilb) / 2 ) * self.tinggi
        print(f"Luas Trapesium = {hasil}")
        return hasil

    def lingkaran(self, phi):
        hasil = 2 * phi * self.r
        print(f"Keliling Lingkaran = {hasil}")
        hasil = phi * self.r * self.r
        print(f"Luas Lingkaran = {hasil}")


bila = int(input("\nMasukkan bilangan pertama : "))
bilb = int(input("Masukkan bilangan kedua   : "))
bilc = int(input("Masukkan bilangan Ketiga : "))
bild = int(input("Masukkan bilangan keempat   : "))
tinggi = int(input("Masukkan Tinggi Bangun Datar : "))
d1 = int(input("Masukkan d1 layang-layang dan belah ketupat : "))
d2 = int(input("Masukkan d2 layang-layang dan belah ketupat : "))
r = int(input("Masukkan bilangan r lingkaran : "))
hasil = None


bangundatar_one = bangundatar(bila, bilb, hasil, tinggi, d1, d2, r, bilc, bild)

print("\n============================")
bangundatar_one.persegi()
print("\n============================")
bangundatar_one.persegipanjang()
print("\n============================")
bangundatar_one.jajargenjang()
print("\n============================")
bangundatar_one.segitiga()
print("\n============================")
bangundatar_one.belahketupat()
print("\n============================")
bangundatar_one.layanglayang()
print("\n============================")
bangundatar_one.trapesium()
print("\n============================")
bangundatar_one.lingkaran(3.14)

