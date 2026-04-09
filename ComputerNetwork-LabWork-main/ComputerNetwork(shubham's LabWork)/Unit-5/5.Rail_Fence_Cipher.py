def rail_fence_encrypt(text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail].append(char)
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    result = ""
    for row in fence:
        result += "".join(row)

    return result


def rail_fence_decrypt(cipher, rails):
    # Create empty matrix
    fence = [['\n' for _ in range(len(cipher))] for _ in range(rails)]

    # Mark zigzag pattern
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        fence[rail][i] = '*'
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    # Fill characters
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if fence[i][j] == '*' and index < len(cipher):
                fence[i][j] = cipher[index]
                index += 1

    # Read zigzag
    result = ""
    rail = 0
    direction = 1

    for i in range(len(cipher)):
        result += fence[rail][i]
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1

    return result


# Input
plaintext = input("Enter plaintext: ")
rails = int(input("Enter number of rails: "))

# Process
cipher = rail_fence_encrypt(plaintext, rails)
decrypted = rail_fence_decrypt(cipher, rails)

# Output
print("Encrypted:", cipher)
print("Decrypted:", decrypted)