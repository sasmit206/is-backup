def findShift(ciphertext, plaintext):

    # Convert both to uppercase for consistent comparison
    ciphertext = ciphertext.upper()
    plaintext = plaintext.upper()

    # Ciphertext and plaintext must have the same length
    if(len(ciphertext) != len(plaintext)):
        return None

    diff = []

    # Find the shift for each corresponding character
    for c, p in zip(ciphertext, plaintext):
        diff.append((ord(c) - ord(p)) % 26)

    # All characters must have the same shift
    if(len(set(diff)) != 1):
        return None

    return diff[0]


def decrypt(ciphertext, key):

    ciphertext = ciphertext.upper()
    plaintext = ""

    for ch in ciphertext:

        c = ord(ch) - ord('A')

        # Caesar decryption: P = (C - key) mod 26
        p = (c - key) % 26

        plaintext += chr(p + ord('A'))

    return plaintext


def main():

    # Known plaintext-ciphertext pair
    cipher = "CIW"
    plain = "YES"

    # Recover the Caesar shift from the known pair
    key = findShift(cipher, plain)

    if key is not None:
        print("Shift =", key)
        print("Attack = Known Plaintext Attack")

        # Decrypt another ciphertext using the recovered key
        print("Plaintext =", decrypt("XVIEWYWI", key))

    else:
        print("Invalid plaintext-ciphertext pair.")


main()