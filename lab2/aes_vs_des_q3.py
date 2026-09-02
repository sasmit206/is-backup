import time

from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad, unpad


# Number of times each encryption/decryption operation is performed.
# Repeating the operation 10,000 times gives a more measurable
# execution time for comparison.
N = 10000


# Message that will be encrypted by both algorithms.
message = b"Performance Testing of Encryption Algorithms"


# DES requires an 8-byte key.
des_key = b"12345678"

# 32-byte AES key = AES-256.
aes_key = b"12345678901234567890123456789012"


# ------------------- DES -------------------

# Record the starting time before DES encryption.
start = time.perf_counter()

# Perform DES encryption N times.
for _ in range(N):

    # Create a new DES cipher using the key and ECB mode.
    des = DES.new(des_key, DES.MODE_ECB)

    # DES has an 8-byte block size.
    # pad() makes the message length a multiple of 8,
    # then encrypt() encrypts the padded message.
    des_ciphertext = des.encrypt(pad(message, 8))


# Calculate total time taken for all N DES encryptions.
des_encrypt_time = time.perf_counter() - start


# ------------------- DES DECRYPTION -------------------

# Record the starting time before DES decryption.
start = time.perf_counter()

# Perform DES decryption N times.
for _ in range(N):

    # Create a DES cipher using the same key and same mode.
    des = DES.new(des_key, DES.MODE_ECB)

    # Decrypt the ciphertext.
    # unpad() removes the padding that was added during encryption.
    des_plaintext = unpad(des.decrypt(des_ciphertext), 8)


# Calculate total time taken for all N DES decryptions.
des_decrypt_time = time.perf_counter() - start


# ------------------- AES -------------------

# Record the starting time before AES encryption.
start = time.perf_counter()

# Perform AES encryption N times.
for _ in range(N):

    # Create an AES cipher using the 32-byte key.
    # 32-byte key means AES-256.
    # ECB specifies the mode of operation.
    aes = AES.new(aes_key, AES.MODE_ECB)

    # AES has a 16-byte block size.
    # pad() makes the message length a multiple of 16,
    # then encrypt() encrypts the padded message.
    aes_ciphertext = aes.encrypt(pad(message, 16))


# Calculate total time taken for all N AES encryptions.
aes_encrypt_time = time.perf_counter() - start


# ------------------- AES DECRYPTION -------------------

# Record the starting time before AES decryption.
start = time.perf_counter()

# Perform AES decryption N times.
for _ in range(N):

    # Create an AES cipher using the same key and same ECB mode.
    aes = AES.new(aes_key, AES.MODE_ECB)

    # Decrypt the ciphertext and then remove the padding.
    aes_plaintext = unpad(aes.decrypt(aes_ciphertext), 16)


# Calculate total time taken for all N AES decryptions.
aes_decrypt_time = time.perf_counter() - start


# ---------------- Results ----------------

# Display the total time taken for 10,000 DES encryptions/decryptions.
print("DES Encryption Time :", des_encrypt_time)
print("DES Decryption Time :", des_decrypt_time)

# Display the total time taken for 10,000 AES-256 encryptions/decryptions.
print("AES-256 Encryption Time :", aes_encrypt_time)
print("AES-256 Decryption Time :", aes_decrypt_time)


# Display the final decrypted messages.
# decode() converts bytes back into a normal Python string.
print("\nDES Decrypted :", des_plaintext.decode())
print("AES Decrypted :", aes_plaintext.decode())