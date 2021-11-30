from Crypto.Cipher import DES
from secrets import token_bytes

key = token_bytes(8)
print("losowy klucz ",key)

def encrypt(msg):
    cipher = DES.new(key, DES.MODE_EAX)
    nonce = cipher.nonce
    print("nonce wfunkcji ",nonce)
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    print("nonce ", nonce)
    print("ciphertext ", ciphertext)
    print("tag ", tag)
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    print("des  cipher", cipher)
    plaintext = cipher.decrypt(ciphertext)

    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext, tag)

print(f'Cipher text: {ciphertext}')
print(f'Cipher text n: ', ciphertext ,'\n')
if not plaintext:
    print('Message is corrupted!')
else:
    print(f'Plain text: {plaintext}')