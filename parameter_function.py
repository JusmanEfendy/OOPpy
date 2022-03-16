def users(name):
    print('Hallo Jussy')
    print('Selamat belajar python')

print('start') # function print menerima paramter string
# users () # ini akan error karena parameter tidak dipanggil
# agar tidak error kita masukkan dulu nilai ke parameternya
users('Jussy') # seperti ini 

print("===================================================")

#solusinya untuk diatas
def users(nama):
    print('Hello ' + nama) # variabel nama bisa disisipkan didalam function pront
    print('Nama anda adalah : ' + nama)
    print('selamat belajar pyhton')

print("========================================================")

users("Jusman")
users("anu")
users("iga")

print("=====================================================")

# solusi untuk menambah 2 parameter 
def user(nama, mk):
    print("Hallo " + nama)
    print('Selamat belajar '+ mk)

# jika hanya memanggil 1 parameter maka akan error, harus sama dengan jumlah parameter
users("Jussy", "Python")
users(nama = "Jussy", mk = "Python") # bisa seperti ini

print("======================================================")

