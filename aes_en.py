#Zuzanna Borkowska (s21243)
#Aleksnader Mazurek (s15023)
import pyAesCrypt
import glob


def encrypt(key, source):
    output = source + ".crypted"
    pyAesCrypt.encryptFile(source, output, key)
    return output


def decrypt(key, source):
    dfile = source.split(".")
    output = dfile[0] + "decrypted." + dfile[1]
    pyAesCrypt.decryptFile(source, output, key)
    return


key = "test_passkey"
while True:
    choice = input('Do you want ?\n 1- encrypt \n 2- decrypt \n 3- exit \nfiles?: ')
    if choice == '3':
        exit(0)
    if choice == '1':
        for file in glob.glob("/Users/Alex/Desktop/BSI2/PY/TEXTVIRUS310/Encrypt_descrypt/test/*.txt"):
            encrypt(key, file)
            print("done")
    # for file in glob.glob("files/*.txt"):
    #     os.remove(file)
    if choice == '2':
        for file in glob.glob('/Users/Alex/Desktop/BSI2/PY/TEXTVIRUS310/Encrypt_descrypt/test/*.crypted'):
            decrypt(key, file)
            print("done")