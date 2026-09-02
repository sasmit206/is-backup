# Basically vignere lagana hai uske upar aes and aes ka key ko transmit Krna hai to
# person B with rsa encryption phir rsa ko decrypt krke aes key milega n then usko 
# decrypt krke vignere laga kr actual code

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from math import gcd


# ============================================================
# PERSON A
# ============================================================

# ================= VIGENERE ENCRYPTION =================

plaintext = input("Enter the plaintext: ")
vig_key = input("Enter the Vigenere key: ")

plaintext = plaintext.lower().replace(' ', '')
vig_key = vig_key.lower().replace(' ', '')

vigenere_ciphertext = ''

for i in range(len(plaintext)):
    p = ord(plaintext[i]) - ord('a')

    k = ord(vig_key[i % len(vig_key)]) - ord('a')

    c = (p + k) % 26

    vigenere_ciphertext += chr(c + ord('a'))

print("Vigenere Ciphertext:", vigenere_ciphertext)


# ============================================================
# AES ENCRYPTION OF VIGENERE CIPHERTEXT
# ============================================================

aes_key = b"0123456789ABCDEF0123456789ABCDEF"

message = vigenere_ciphertext.encode()

cipher = AES.new(aes_key, AES.MODE_ECB)

aes_ciphertext = cipher.encrypt(pad(message, 16))

print("AES Ciphertext:", aes_ciphertext.hex())


# ============================================================
# RSA KEY GENERATION
# Person B's RSA key pair
# ============================================================

p = 10007
q = 10009

n = p * q
phi = (p - 1) * (q - 1)

e = -1

for i in range(2, phi):
    if gcd(i, phi) == 1:
        e = i
        break

d = -1

for i in range(1, phi):
    if (e * i) % phi == 1:
        d = i
        break

print("\nRSA Parameters")
print("n =", n)
print("phi =", phi)
print("e =", e)
print("d =", d)


# ============================================================
# RSA ENCRYPTION OF AES KEY
# Person A uses Person B's PUBLIC KEY (e,n)
# ============================================================

encrypted_aes_key = []

for byte in aes_key:

    # AES key is bytes, so directly use byte value
    M = byte

    # RSA encryption
    C = pow(M, e, n)

    encrypted_aes_key.append(C)

print("\nRSA Encrypted AES Key:")
print(encrypted_aes_key)


# ============================================================
# TRANSMISSION
# ============================================================

# Person A sends:
#
# 1. AES ciphertext
# 2. RSA encrypted AES key
#
# Person B has:
# 1. RSA private key (d,n)
# 2. Vigenere key


# ============================================================
# PERSON B
# ============================================================

# ================= RSA DECRYPTION =================

decrypted_aes_key = bytearray()

for C in encrypted_aes_key:

    # RSA decryption
    M = pow(C, d, n)

    decrypted_aes_key.append(M)

decrypted_aes_key = bytes(decrypted_aes_key)

print("\nRecovered AES Key:")
print(decrypted_aes_key)


# ============================================================
# AES DECRYPTION
# ============================================================

cipher = AES.new(decrypted_aes_key, AES.MODE_ECB)

decrypted_padded = cipher.decrypt(aes_ciphertext)

decrypted_vigenere = unpad(
    decrypted_padded,
    16
).decode()

print("\nRecovered Vigenere Ciphertext:")
print(decrypted_vigenere)


# ============================================================
# VIGENERE DECRYPTION
# ============================================================

original_plaintext = ''

for i in range(len(decrypted_vigenere)):

    c = ord(decrypted_vigenere[i]) - ord('a')

    k = ord(vig_key[i % len(vig_key)]) - ord('a')

    p = (c - k) % 26

    original_plaintext += chr(p + ord('a'))


print("\nOriginal Plaintext:")
print(original_plaintext)
