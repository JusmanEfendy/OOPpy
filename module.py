'''
Modul
    digunakan untuk mengelompokkan function-function sesuai dengan kegunaannya
    coontoh:
    pada matematika.py
    disana ada tambah dan kurang
'''

import fisika
result = fisika.kecepatan(10,5)
print(result)

print('===================================')

#cara lain yang lebih efisien
from fisika import kecepatan, waktu_tempuh
cek = kecepatan(5,10)
cek1 = waktu_tempuh(15,10)
print(cek)
print(cek1)

print("=====================================")