import random


normal = list(" abcdefghijklmnopqrstuvwxyz")
secret = normal.copy()
random.shuffle(secret)


def encrypt_message(message, normal, secret):
    cipher_text = ""
    for letter in message:
        lower = letter.lower()
        if lower in normal:
            position = normal.index(lower)
            sub = secret[position]
            cipher_text += sub.upper() if letter.isupper() else sub
        else:
            cipher_text += letter
    return cipher_text


if __name__ == "__main__":
    message = input("Enter a message to encrypt: ")
    cipher_text = encrypt_message(message, normal, secret)
    print(f"Original message: {message}")
    print(f"Encrypted message: {cipher_text}")
