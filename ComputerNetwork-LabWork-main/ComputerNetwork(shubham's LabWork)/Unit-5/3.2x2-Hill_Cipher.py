import numpy as np

# Function to find modular inverse
def mod_inverse(a, m):
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Encryption
def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    
    if len(text) % 2 != 0:
        text += 'X'  # Padding

    key_matrix = np.array(key).reshape(2, 2)
    result = ""

    for i in range(0, len(text), 2):
        pair = np.array([[ord(text[i]) - 65], [ord(text[i+1]) - 65]])
        cipher = np.dot(key_matrix, pair) % 26

        result += chr(cipher[0][0] + 65)
        result += chr(cipher[1][0] + 65)

    return result

# Decryption
def hill_decrypt(cipher, key, original_length):
    key_matrix = np.array(key).reshape(2, 2)
    
    a, b = key_matrix[0]
    c, d = key_matrix[1]

    det = int((a * d - b * c) % 26)
    inv_det = mod_inverse(det, 26)

    if inv_det is None:
        raise ValueError("Key not invertible!")

    adj = np.array([[d, -b], [-c, a]]) % 26
    inv_key = (inv_det * adj) % 26

    result = ""

    for i in range(0, len(cipher), 2):
        pair = np.array([[ord(cipher[i]) - 65], [ord(cipher[i+1]) - 65]])
        plain = np.dot(inv_key, pair) % 26

        result += chr(int(plain[0][0]) + 65)
        result += chr(int(plain[1][0]) + 65)

    return result[:original_length]  # Remove padding

# Input
plaintext = input("Enter plaintext: ")
key = [[3, 4], [2, 3]]

# Process
cipher = hill_encrypt(plaintext, key)
decrypted = hill_decrypt(cipher, key, len(plaintext))

# Output
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", cipher)
print("Decrypted:", decrypted)