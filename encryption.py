import random


normal = list(" abcdefghijklmnopqrstuvwxyz")
secret = normal.copy()
random.shuffle(secret)

def encrypt_message(message, normal, secret):
    cipher_text = ""
    for letter in message:
        if letter in normal:
            position = normal.index(letter)
            cipher_text += secret[position]
        else:
            cipher_text += letter
    return cipher_text


if __name__ == "__main__":
    message = input("Enter a message to encrypt: ").lower()
    cipher_text = encrypt_message(message, normal, secret)
    print(f"original message: {message}")
    print(f"Encrypted message: {cipher_text}")