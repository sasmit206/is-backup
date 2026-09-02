def playfair_encrypt(text, key):

    # Convert to lowercase, remove spaces, and replace j with i
    text = text.lower().replace(" ", "").replace("j", "i")
    key = key.lower().replace("j", "i")

    # Remove duplicate letters from the key
    key = "".join(dict.fromkeys(key))

    # Playfair uses a 5×5 matrix, so i and j share one position
    alphabet = "abcdefghiklmnopqrstuvwxyz"

    # Put the key first, then append unused alphabet letters
    letters = key + "".join(c for c in alphabet if c not in key)

    # Create the 5×5 Playfair matrix
    matrix = [letters[i:i+5] for i in range(0, 25, 5)]

    pairs = []
    i = 0

    # Divide plaintext into pairs
    while i < len(text):

        a = text[i]

        # If one character is left, add 'x'
        if i + 1 == len(text):
            pairs.append(a + "x")
            break

        b = text[i+1]

        if a == b:
            # Same letters cannot occur in one pair, so insert x
            pairs.append(a + "x")
            i += 1

        else:
            pairs.append(a + b)
            i += 2

    cipher = ""

    # Encrypt each pair
    for a, b in pairs:

        # Row and column positions of the two letters
        r1, c1, r2, c2 = 0, 0, 0, 0

        # Find positions of a and b in the matrix
        for r in range(5):
            for c in range(5):

                if matrix[r][c] == a:
                    r1, c1 = r, c

                if matrix[r][c] == b:
                    r2, c2 = r, c

        # Same row → move each letter one position to the right
        if r1 == r2:
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        # Same column → move each letter one position downward
        elif c1 == c2:
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        # Different row and column → rectangle rule
        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def main():
    # Change plaintext and key here if required
    print(playfair_encrypt(
        "The key is hidden under the door pad",
        "GUIDANCE"
    ))


main()