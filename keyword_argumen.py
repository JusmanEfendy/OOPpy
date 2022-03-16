def user(nama, mk):
    print("Hallo " , nama)
    print('Selamat belajar ', mk)

#misalnya kita panggil seperti ini
user("Pyton", "Jussy") # maka hasilnya akan kebalik

#solusinya
def user(nama, mk):
    print("halo ", nama)
    print("selamat belajar", mk)

user(mk = "Python", nama = "Jussy") # hasilnya sama
user(nama = "Jussy", mk = "Python") # sama

'''
sebenarnya didalam perkodingan kita sering menggunakan positional argumen
tapi untuk kasus yang kompleks dan argumennya banyak positional argumen

contoh

def harga_hewan(sapi, kambing, rusa, babi, kerbau, domba):
    pass

    harga_hewan(100,829,282,274,422,428)

ribet dan susah dibaca untuk programmer lainnya, untuk kasus diatas 
disarankan menggunakan keyword argumen

harusnya seperti ini

    harga_hewan(sapi = 737, babi = 382, kambing = 738)
'''