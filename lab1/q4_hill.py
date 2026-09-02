k = []

# Change m to change the size of the key matrix (m × m)
m = int(input("Enter the dimension of Key matrix: "))


# Read the key matrix from the user
for i in range(m):
    subarr = []

    for j in range(m):
        subarr.append(int(input()))

    k.append(subarr)


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
            temp.append(ord(plaintext[i+j]) - ord('a'))


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


def hill_decrypt(ciphertext):
    # Decryption requires the inverse of the key matrix modulo 26
    count = (m - len(ciphertext) % m) % m
    plaintext = ''


def main():

    # Change the plaintext here if required
    plaintext = input("Enter the plaintext: ").lower().replace(' ', '')

    ciphertext = hill_encrypt(plaintext)

    print(ciphertext)


main()