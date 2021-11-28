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
    print('choose of the following operations: \n\t 1 -Encrypt\n\t 2- Decrypt \n 3- exit')
    choice = input("Your choice: ")
    if choice == '3':
        exit(0)
    if choice not in ['1', '2']:
        break

    root_dir = '/Users/Alex/Desktop/BSI2/PY/TEXTVIRUS310/test/'
    end_dir =  '*.txt' #input("input path text:")
    file_path = root_dir + end_dir

    key = "test_passkey"  # input("encrypted key: ")

    key_hash = md5(key.encode('ascii')).digest()  # 16bit hask
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    if choice == '1':
        for file in glob.glob(file_path):
            encryptall(file)

    if choice == '2':
        for file in glob.glob(file_path):
            descryptall(file)