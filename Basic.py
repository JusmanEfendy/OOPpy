class kendaraan: # Template

    def __init__(self, Type, Warna, kecepatan): # Atribut
        self.type = Type
        self.warna = Warna
        self.kecepatan = kecepatan
        
    # method
    def maju(self, up):
        gass = self.kecepatan + up
        print(self.type + ' '+ self.warna + ' Menambah kecepatan menjadi', gass, 'km/h')

    def stop(self, kendaraan):
        print(self.type + ' ' + self.warna + ' Parkir di samping ' + kendaraan.type + ' ' +kendaraan.warna)

    def kurang(self, min):
        rem = self.kecepatan - min
        print(self.type + ' ' + self.warna+ ' ' + 'Mengurangi Kecepatan menjadi ' , rem, 'km/h')

kendaraan1 = kendaraan('Sedan', 'Merah', 100)
kendaraan2 = kendaraan('Truk', 'Kuning', 60)


kendaraan2.stop(kendaraan1)
kendaraan1.maju(70)
kendaraan1.kurang(50)
