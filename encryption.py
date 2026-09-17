import random


normal = list(" abcdefghijklmnopqrstuvwxyz")
secret = normal.copy()
random.shuffle(secret)

message = input("enter a letter: ").lower()

cipher_text=  ""

for letter in message:
    position = normal.index(letter)
    secret_num = secret[position]
    cipher_text+= secret_num



print(f"original messhe: {message}")
print(f"Encrypted message: {cipher_text}")