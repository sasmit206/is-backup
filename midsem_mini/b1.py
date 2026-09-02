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

def affine_encrypt(plaintext, k1, k2):
    cipher = ""

    for ch in plaintext:
        if 'a'<=ch<='z':
            p = ord(ch) - ord('a')
        elif 'A'<=ch<='Z':
            p=ord(ch)-ord('A')+26

        # Affine encryption: C = (P*k1 + k2) mod 26
        c = (p * k1 + k2) % 52

        if c<=25:
            cipher += chr(c + ord('a'))
        elif c<=51:
            cipher += chr(c + ord('A'))
    return cipher




def hill_encrypt(plaintext):

    # Add 'x' padding so plaintext length is a multiple of m
    count = (m - len(plaintext) % m) % m
    plaintext += 'x' * count

    ciphertext = ''

    # Process plaintext in blocks of m characters
    for i in range(0, len(plaintext), m):

        temp = []
        c = []

        # Convert characters to numbers:
        # a=0, b=1, ..., z=25
        for j in range(m):
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

            # Apply modulo 26
            c.append(total % 26)


        # Convert numbers back to characters
        for x in c:
            ciphertext += chr(x + ord('a'))

    return ciphertext

def main():
    pt=input("Enter plaintext : ")
    pt = ''.join(ch for ch in pt if ch.isalpha())
    k1=int(input("Enter value of k1"))
    while gcd(k1, 52) != 1:       # Only k1 must be coprime with 26
        k1=int(input("Enter valid k1"))
    k2=int(input("Enter k2:"))
    ct1=affine_encrypt(pt,k1,k2)
    ct2=hill_encrypt(ct1)
    print(ct1)
    print(ct2)


main()