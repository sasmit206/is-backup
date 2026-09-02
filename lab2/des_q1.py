# Import the DES cipher implementation from the Crypto library
from Crypto.Cipher import DES

# Import functions for adding and removing padding
from Crypto.Util.Padding import pad, unpad


# Define the DES key.
# DES requires an 8-byte (64-bit) key.
key = b"A1B2C3D4"

# Plaintext message to be encrypted.
# The 'b' indicates this is stored as bytes instead of a normal string.
message = b"Confidential Data"


# ---------------- ENCRYPTION ----------------

# Create a DES cipher object.
# key          -> Secret key used for encryption
# DES.MODE_ECB -> ECB (Electronic Codebook) mode
cipher = DES.new(key, DES.MODE_ECB)

# pad(message, 8)
# Since DES works on 8-byte blocks, pad() adds extra bytes
# if the message length is not a multiple of 8.
#
# cipher.encrypt(...)
# Encrypts the padded message using DES.
ciphertext = cipher.encrypt(pad(message, 8))

# Convert ciphertext bytes into hexadecimal so it is readable.
print("Ciphertext:", ciphertext.hex())


# ---------------- DECRYPTION ----------------

cipher = DES.new(key, DES.MODE_ECB)

# cipher.decrypt(ciphertext)
# Decrypts the ciphertext.
#
# Result still contains the padding bytes that were added earlier.
#
# unpad(..., 8)
# Removes those padding bytes to recover the original message.
plaintext = unpad(cipher.decrypt(ciphertext), 8)

print("Decrypted:", plaintext.decode())

#python -m venv .venv
#.venv\Scripts\activate
#python -m pip install pycryptodome