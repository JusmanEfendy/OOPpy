'''
package
    kumpulan kode yang berada dalam 1 folder .py
    bisa kumpulan dari beberapa modul atau sebagainya
    syarat sauatu folder untuk menjadi package harus ada file yang namanya __init__.py
    sudah confension dari python
    sudah dibuat package rumus dimana didalamnya bernama matik.py
    dengan function kecepatan dan waktu_tempuh
'''

from rumus import matik
result = matik.tambah(2,3)
result1 = matik.kurang(5,2)

print(result)
print(result1)

print("========================================")

# cara lain
from rumus.matik import tambah,kurang

result = tambah(2,5)
result1 = kurang(5,3)

print(result)
print(result1)

print("==========================================="))
