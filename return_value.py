'''
Return value
    1. Biasanya disebut dengan return statement
    2. jadi nilai yang dikembalikan dari operasi sebuah function
    3. contoh
        len() --> digunakan untuk mengembalikan panjang dari variabel

'''

data = "Jussy"
lenght = len(data)

print("Bernilai : ", lenght) # akan bernilai 5. saat kita memanggil function len
                            # maka len akan mengembalikan sebuah nilai kemudian 
                            # disimpan didalam variabel lenght


#Return Value part 2

# contoh tidak bagus
def user(nama, mk):
    print("halo ", nama)
    print("selamat belajar", mk)

temp = user("Jussy", " Python")
print(temp)

print("===========================================")

# contoh yang bagus
# hasilnya
def multiply(number_1, number_2):
    result = number_1 * number_2
    return result # secara eksplisit, bahwa balikannya adalah result,
                    # maka output akan bernilai result
output = multiply(2,5)
print(output)
'''
1. input  : (number1, number2)
2. proses : number1 * number2
3. output : result --> untuk mengeluarkan output kita harus menggunakan keyword return
'''
# bisa juga untuk mempersingkat kodingan seperti iini
def multiply(number1, number2):
    return number1 * number2
print(multiply(2,5))

print('================================================')