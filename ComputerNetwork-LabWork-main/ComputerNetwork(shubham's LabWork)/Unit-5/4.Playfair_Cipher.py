def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []

    for char in key:
        if char not in matrix and char.isalpha():
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)

    return [matrix[i*5:(i+1)*5] for i in range(5)]


def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'

        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2

    if len(pairs[-1]) == 1:
        pairs[-1] += 'X'

    return pairs


def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    pairs = prepare_text(text)

    result = ""

    for a, b in pairs:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


def playfair_decrypt(cipher, key):
    matrix = generate_matrix(key)
    result = ""

    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


# Input
plaintext = input("Enter plaintext: ")
key = input("Enter key: ")

# Process
cipher = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(cipher, key)

# Output
print("Ciphertext:", cipher)
print("Decrypted text:", decrypted)