def RSA(plaintext):
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

    print("n =", n)
    print("phi =", phi)
    print("e =", e)
    print("d =", d)

    ciphertext = []

    # Encryption: C = M^e mod n
    for ch in plaintext:
        M = ord(ch) - ord('a')
        C = pow(M, e, n)
        ciphertext.append(C)

    return ciphertext, d, n


def decrypt(ciphertext, d, n):
    plaintext = ""

    # Decryption: M = C^d mod n
    for C in ciphertext:
        M = pow(C, d, n)
        plaintext += chr(M + ord('a'))

    return plaintext


def main():
    plaintext = "Asymmetric Encryption"
    plaintext = plaintext.lower().replace(" ", "")

    ciphertext, d, n = RSA(plaintext)

    print("\nCiphertext:", ciphertext)

    decrypted = decrypt(ciphertext, d, n)

    print("Decrypted:", decrypted)


main()