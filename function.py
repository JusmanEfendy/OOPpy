'''
function atau fungsi pada python
    1. kita sudah banyak sekali menggunakan function bawaan dari python
    2. contohnya
        - print()
        - input()
    3. function sebenarnya adalah kumpulan dari intruksi atau perintah yang
        dibungkus menjadi sebuah kesatuan
    4. didalam function sebenarnya ada 1 atau lebih dari 1 baris kode
    5. biasanya function kita gunakan untuk mengelompokkan intrusi-intruksinya memiliki
        tujuan khusus dan kita kasih nama 
        print()
        tujuannya : digunakan untuk mencetak suatu tulisan ke terminal program kita
        input()
        tujuannya: digunakan untuk menangkap inputan dari user kemudian bisa di simpan
        kedalam variabel
    6. function : bisa digunakan berulang kali , walaupun pendefinisiannya hanya sekali
    7. konsep : bungkus kumpulan kode tertentu untuk tujuan yang sama (spesifik)

        def users(args):
            pass

        def : keywoard untuk mendefinisikan function
        users : nama function
        args : parameter function
        pass: passing (bagian dari function) bodi : code
'''


#contoh sederhana

def users():
    print("Hello Jussy")
    print("Selamat belajar python")
print("diluar function")

users() # tidak bisa dipanggil sebelum function didefinisikan
print(users()) # cara lain agar bisa memanggil function

print("=========================================")

def tambah (a,b): # a dan b adalah parameter
    result = a + b
    return result
print (tambah(2,5)) # nilai parameter bisa diisi disini

print("===========================================")

def biodata (nama, alamat):
    print("Nama : ", nama)
    print("Alamat : ", alamat)
print(biodata("Jussy", "Teluk Santong"))

