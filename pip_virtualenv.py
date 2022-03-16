'''
pip dan virtual environment
    bagaimana cara kita menggunakan codingan orang lain
    atau menginsallnya pada directory kita 
    dan cara kita menggunakannya pada project python kita

caranya : 
    1. https://pypi.org
    2. example : cowsay
    3. tinggal di klik
    4. cara installnya lengkap documentasinya
    5. jika saat menjalankan pip install cowsay error, maka disarankan untuk menggunakan
        virtual environment
    6. kunjungi situs tutorial installing package 
    7. py -m pip install --user virtualenv
    8. WARNING : The script virtualenv.exe is installed
    9. berarti proses install selesai

cara lain:
    1. masuk terminal atau vscode
    2. python --version
    3. python (mencoba program)
    4. python -m venv newProject (membuat venv)
    5. PS c:\00 python (nama folder) (membuka vscode)
    6. cd scripts
    7. ./activate
'''

import cowsay

cowsay.cow('Helo Jussy')

print('==========================')