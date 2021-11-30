#Zuzanna Borkowska (s21243)
#Aleksnader Mazurek (s15023)
import glob
from Crypto.Cipher import DES3
from hashlib import md5

def encryptall(file_path):
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        new_file_bytes = cipher.decrypt(file_bytes)
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)

def descryptall(file_path):
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        new_file_bytes = cipher.decrypt(file_bytes)
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)

while True:
    print('choose of the following operations: \n1-Encrypt\n2-Decrypt\n3-exit')
    choice = input("Your choice: ")
    if choice == '3':
        exit(0)
    if choice not in ['1', '2']:
        break

    file_path = '/Users/Alex/Desktop/BSI2/PY/TEXTVIRUS310/Encrypt_descrypt/test/*.txt'

    key = "test_passkey"  # input("key: ")

    key_hash = md5(key.encode('ascii')).digest()  # 16bit hask
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    if choice == '1':
        for file in glob.glob(file_path):
            encryptall(file)

    if choice == '2':
        for file in glob.glob(file_path):
            descryptall(file)