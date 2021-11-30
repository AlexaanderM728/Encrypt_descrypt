from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)

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

file_path = '/Users/Alex/Desktop/BSI2/PY/TEXTVIRUS310/test/read.txt'
text_file = open(file_path, 'r+')
text_data = text_file.read()
print('otwarty:',text_data)

nonce, ciphertext, tag = encrypt(text_data)
print("zaszyfrowant:" ,ciphertext)
text_file.close()
text_file = open(file_path, 'rb')
text_data = text_file.read()
text_file.write(rep)
(text_data,'\n')



text_file = open(file_path, 'r+')
text_data = text_file.read()


plaintext = decrypt(nonce, ciphertext, tag)

text_file.close()
print(f'Cipher text: {ciphertext}')

if not plaintext:
    print('Message is corrupted!')
else:
    print(f'Plain text: {plaintext}')