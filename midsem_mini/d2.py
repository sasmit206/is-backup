# Basically vignere lagana hai uske upar aes and aes ka key ko transmit Krna hai to
# person B with rsa encryption phir rsa ko decrypt krke aes key milega n then usko 
# decrypt krke vignere laga kr actual code

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

#=================Vignere cipher encrypt

#Vignere encryption
plaintext=input("Enter the plaintext: ")
key=input("Enter the key: ")
plaintext = plaintext.lower().replace(' ', '')
key = key.lower().replace(' ', '')

ciphertext = ''

for i in range(len(plaintext)):
    p = ord(plaintext[i]) - ord('a')

    # Key repeats using i % len(key)
    k = ord(key[i % len(key)]) - ord('a')

    c = (p + k) % 26
    ciphertext += chr(c + ord('a'))


#===========================Encrypt vignere op using AES

key = b"0123456789ABCDEF0123456789ABCDEF"

# Plaintext message to encrypt.
# 'b' means the message is stored as bytes.
message =  ciphertext.encode()


# ---------------- ENCRYPTION ----------------

# Create an AES cipher object using the given key and ECB mode.
cipher = AES.new(key, AES.MODE_ECB)

# AES has a block size of 16 bytes.
# pad() adds padding so the message length becomes a multiple of 16.
# encrypt() then encrypts the padded message.
ciphertext = cipher.encrypt(pad(message, 16))

# Convert the encrypted bytes to hexadecimal for readable display.
print("Ciphertext: ", ciphertext.hex())


# ---------------- DECRYPTION ----------------

# Create an AES cipher object using the same key and same mode.
cipher = AES.new(key, AES.MODE_ECB)

# First decrypt the ciphertext.
# The result still contains the padding added during encryption.
#
# unpad() removes that padding and gives us the original plaintext.
plaintext = unpad(cipher.decrypt(ciphertext), 16)

# Convert the decrypted bytes back into a normal string.
print("Decrypted: ", plaintext.decode())



#######################Encrypt AES key using RSA

from math import gcd



p = 10007
q = 10009

n = p * q
phi = (p - 1)*(q - 1)


e = -1

for i in range(2,phi):
    if gcd(i,phi) == 1:
        e = i
        break

d = -1
for i in range (1, phi):
    if (e * i) % phi == 1:
        d = i
        break

key_aes_rsa = []

for ch in key.decode():
    M = ord(ch) - ord('a')
    C = pow(M,e,n)
    key_aes_rsa.append(C)

print("Encrypted AES key using RSA: ", key_aes_rsa)


# Decryption: M = C^d mod n
d_key_aes_rsa="h"
for C in key_aes_rsa:
    M = pow(C, d, n)
    d_key_aes_rsa += chr(M + ord('a'))
print("Decrypted AES key using RSA: ", d_key_aes_rsa)