from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# AES key.
# AES accepts 16, 24, or 32-byte keys.
# This key is 32 bytes = AES-256.
key = b"0123456789ABCDEF0123456789ABCDEF"

# Plaintext message to encrypt.
# 'b' means the message is stored as bytes.
message = b"Sensitive Information"


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