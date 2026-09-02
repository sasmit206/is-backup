def findInv(key):
    # Find multiplicative inverse of key modulo 26
    for i in range(26):
        if (i * key) % 26 == 1:
            return i
    return -1


def affine_encrypt(plaintext, k1, k2):

    plaintext = plaintext.upper()
    cipher = ""

    for ch in plaintext:

        p = ord(ch) - ord('A')

        # Affine encryption: C = (P*k1 + k2) mod 26
        c = (p * k1 + k2) % 26

        cipher += chr(c + ord('A'))

    return cipher


def affine_decrypt(ciphertext, k1, k2):

    # k1 must have a multiplicative inverse modulo 26
    inv = findInv(k1)

    ciphertext = ciphertext.upper()
    plaintext = ""

    for ch in ciphertext:

        c = ord(ch) - ord('A')

        # Affine decryption: P = (C-k2)*k1^-1 mod 26
        p = ((c - k2) * inv) % 26

        plaintext += chr(p + ord('A'))

    return plaintext


def bruteForce(ciphertext):

    # Known plaintext-ciphertext pair:
    # "AB" encrypts to "GL"
    target = "GL"

    # Try every possible k1
    for k1 in range(26):

        # Skip k1 values that have no inverse modulo 26
        if findInv(k1) == -1:
            continue

        # Try every possible k2
        for k2 in range(26):

            # Check whether this key encrypts AB to GL
            if affine_encrypt("AB", k1, k2) == target:

                print("Key found")
                print("K1 =", k1)
                print("K2 =", k2)

                # Use the discovered key to decrypt the ciphertext
                plain = affine_decrypt(ciphertext, k1, k2)

                print("Plaintext =", plain)
                return

    print("Key not found")


def main():

    # Change ciphertext here if required
    ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"

    bruteForce(ciphertext)


main()