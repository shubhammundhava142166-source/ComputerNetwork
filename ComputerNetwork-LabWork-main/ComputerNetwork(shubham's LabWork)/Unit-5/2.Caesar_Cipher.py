def caesar_cipher(message, shift):
    result = ""

    for char in message:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


# Input
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

# Encryption
encrypted = caesar_cipher(message, shift)
print("Encrypted message:", encrypted)

# Decryption (reverse shift)
decrypted = caesar_cipher(encrypted, -shift)
print("Decrypted message:", decrypted)