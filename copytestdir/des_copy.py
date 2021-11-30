from Crypto.Cipher import DES3
from hashlib import md5


def encryptall(file_path, cipher):
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
    print('choose of the following operations: \n\t 1 -Encrypt\n\t 2- Decrypt')
    operation = input("Your choice: ")
    if operation not in ['1', '2']:
        break

    root_dir = '/test/'
    end_dir = input("input path text:")
    file_path = root_dir + end_dir

    key = "test_passkey"  # input("encrypted key: ")

    key_hash = md5(key.encode('ascii')).digest()  # 16bit hask
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    if operation == '1':
        encryptall(file_path, cipher)
    if operation == '2':
        descryptall(file_path)