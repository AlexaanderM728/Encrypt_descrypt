#Zuzanna Borkowska (s21243)
#Aleksnader Mazurek (s15023)
from Crypto.Cipher import DES
from secrets import token_bytes
import glob
import re

#key = token_bytes(8)
key = b'\xa6\xa4m\xdf\x12\xfa\t{'
print("losowy klucz:", key)


def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag


def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


ciphertext_tab = []
nonce_tab = []
tag_tab = []

while True:
    choice = input('Do you want ?\n 1- encrypt \n 2- decrypt \n 3- exit \nfiles?: ')
    if choice == '3':
        exit(0)
    if choice == '1':
        for file in glob.glob("/Users/Alex/Desktop/BSI2/PY/TEXTVIRUS310/Encrypt_descrypt/test/*.txt"):
             with open(file, "r+") as f:
                nonce, ciphertext, tag = encrypt(f.read())
                ciphertext_tab.append(ciphertext)
                nonce_tab.append(nonce)
                tag_tab.append(tag)
                f.seek(0)
                f.write(re.sub('[^a-zA-Z0-9 \n\.]', '', ciphertext.__str__()))
                #f.truncate()
                #f.write("sfsgadgg")

    if choice == '2':
        i = 0
        for file in glob.glob("/Users/Alex/Desktop/BSI2/PY/TEXTVIRUS310/Encrypt_descrypt/test/*.txt"):
            with open(file, "r+") as f:
                nonce = nonce_tab[i]
                tag = tag_tab[i]
                ciphertext = ciphertext_tab[i]
                plaintext = decrypt(nonce, ciphertext , tag)
                f.truncate()
                f.write(plaintext)
                i+= 1