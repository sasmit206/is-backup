# Question was basically,
# Affine cipher+hill cipher...

# We had a character space of 52, including both uppercase and lowercase letters, a-z (0-25) and A-Z (26-51)
# 1)We had to input plaintext (case sensitive obviously), we had to remove any other character/number from the plaintext apart from alphabets..
# 2)the next step was to input k1, k2 values for affine cipher, and check if GCD(k1,52) is 1 or not, if it's not 1, then prompt the user to re enter k1 value
# 3)the next step was to encrypt the plaintext using affine cipher
# 4)whatever ciphertext we got after applying affine cipher, we had to treat it as plaintext for hill cipher... And then encrypt it using hill cipher..... And one more thing before encrypting we had to ensure proper padding and stuff

# Next stage was decryption:
# 5) decrypt the obtained final ciphertext using hill cipher
# 6) and then decrypt again using affine cipher
# 7) remove any padding if present

from math import gcd


# ---------------------------------------------------------
# Convert character to number
# a-z -> 0-25
# A-Z -> 26-51
# ---------------------------------------------------------
def char_to_num(ch):
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a')
    else:
        return ord(ch) - ord('A') + 26


# ---------------------------------------------------------
# Convert number to character
# 0-25 -> a-z
# 26-51 -> A-Z
# ---------------------------------------------------------
def num_to_char(x):
    if x <= 25:
        return chr(x + ord('a'))
    else:
        return chr(x - 26 + ord('A'))


# ---------------------------------------------------------
# Affine Encryption
# C = (P * k1 + k2) mod 52
# ---------------------------------------------------------
def affine_encrypt(plaintext, k1, k2):
    cipher = ""

    for ch in plaintext:

        p = char_to_num(ch)

        # Affine encryption
        c = (p * k1 + k2) % 52

        cipher += num_to_char(c)

    return cipher


# ---------------------------------------------------------
# Affine Decryption
# P = k1_inverse * (C - k2) mod 52
# ---------------------------------------------------------
def affine_decrypt(ciphertext, k1, k2):

    plaintext = ""

    # Find multiplicative inverse of k1 modulo 52
    k1_inverse = pow(k1, -1, 52)

    for ch in ciphertext:

        c = char_to_num(ch)

        p = (k1_inverse * (c - k2)) % 52

        plaintext += num_to_char(p)

    return plaintext


# ---------------------------------------------------------
# Hill Encryption
# C = K x P mod 52
# ---------------------------------------------------------
def hill_encrypt(plaintext):

    # Add 'x' padding so plaintext length is a multiple of m
    count = (m - len(plaintext) % m) % m
    plaintext += 'x' * count

    ciphertext = ''

    # Process plaintext in blocks of m characters
    for i in range(0, len(plaintext), m):

        temp = []
        c = []

        # Convert characters to numbers
        for j in range(m):

            ch = plaintext[i + j]

            if 'a' <= ch <= 'z':
                temp.append(ord(ch) - ord('a'))
            else:
                temp.append(ord(ch) - ord('A') + 26)

        # Matrix multiplication:
        # C = K × P
        for row in range(m):

            total = 0

            for col in range(m):
                total += k[row][col] * temp[col]

            # Apply modulo 52
            c.append(total % 52)

        # Convert numbers back to characters
        for x in c:
            ciphertext += num_to_char(x)

    return ciphertext


# ---------------------------------------------------------
# Hill Decryption
# C = K x P
# P = K_inverse x C
# ---------------------------------------------------------
def hill_decrypt(ciphertext):

    plaintext = ''

    # Find determinant
    determinant = (
        k[0][0] * k[1][1]
        - k[0][1] * k[1][0]
    )

    determinant = determinant % 52

    # Find inverse of determinant modulo 52
    determinant_inverse = pow(determinant, -1, 52)

    # Inverse matrix of 2x2 matrix
    inverse_k = [
        [
            (k[1][1] * determinant_inverse) % 52,
            (-k[0][1] * determinant_inverse) % 52
        ],
        [
            (-k[1][0] * determinant_inverse) % 52,
            (k[0][0] * determinant_inverse) % 52
        ]
    ]

    # Process ciphertext in blocks of m characters
    for i in range(0, len(ciphertext), m):

        temp = []
        p = []

        # Convert characters to numbers
        for j in range(m):

            ch = ciphertext[i + j]

            if 'a' <= ch <= 'z':
                temp.append(ord(ch) - ord('a'))
            else:
                temp.append(ord(ch) - ord('A') + 26)

        # Matrix multiplication:
        # P = K_inverse × C
        for row in range(m):

            total = 0

            for col in range(m):
                total += inverse_k[row][col] * temp[col]

            # Apply modulo 52
            p.append(total % 52)

        # Convert numbers back to characters
        for x in p:
            plaintext += num_to_char(x)

    return plaintext


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------
def main():

    global m, k

    # Input plaintext
    pt = input("Enter plaintext: ")

    # Remove anything other than English alphabets
    pt = ''.join(
        ch for ch in pt
        if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')
    )

    # Input affine keys
    k1 = int(input("Enter value of k1: "))

    while gcd(k1, 52) != 1:
        k1 = int(input("Enter valid k1: "))

    k2 = int(input("Enter k2: "))

    # -----------------------------------------------------
    # Hill cipher key
    # -----------------------------------------------------
    m = 2

    k = [
        [3, 3],
        [2, 5]
    ]

    # -----------------------------------------------------
    # Encryption
    # -----------------------------------------------------

    # Step 1: Affine encryption
    ct1 = affine_encrypt(pt, k1, k2)

    # Step 2: Hill encryption
    ct2 = hill_encrypt(ct1)

    print("\nAfter Affine Encryption:", ct1)
    print("Final Ciphertext:", ct2)

    # -----------------------------------------------------
    # Decryption
    # -----------------------------------------------------

    # Step 3: Hill decryption
    decrypted_hill = hill_decrypt(ct2)

    # Step 4: Affine decryption
    decrypted_affine = affine_decrypt(
        decrypted_hill,
        k1,
        k2
    )

    # Step 5: Remove padding
    decrypted_plaintext = decrypted_affine.rstrip('x')

    print("\nAfter Hill Decryption:", decrypted_hill)
    print("After Affine Decryption:", decrypted_affine)
    print("Final Decrypted Plaintext:", decrypted_plaintext)


main()
