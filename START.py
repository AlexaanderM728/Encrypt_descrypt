import os

while True:
    choice = input("choice:\n 1- DES3\n 2- AES\n 3- DES\n 4- exit")
    if choice == '4':
        exit(0)
    if choice == '1':
        os.system('python DES3.py')
    if choice == '2':
        os.system('python aes_en.py')
    if choice == '3':
        os.system('python DES.py')