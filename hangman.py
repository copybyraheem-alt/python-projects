secret_word = "apple"
health = 6
display = ["_", "_", "_", "_", "_"]


print("-----------HANGMAN----------")
print(f"guess: {display}")
print(f"your health: {health}")

while True:
    guess = input("guess a letter: ").lower()
    if guess in secret_word:
        position= 0

        for letter in secret_word:
            if letter == guess:
                display[position]=guess
            position+=1
    else:
        health -= 1
        print("nope guess")

    print(f"your current health is: {health}")
    print(f"guess: {display}")
    print("---------------------")
    if health ==0:
        print("Game-over!, you died")
        break
    if "_" not in display:
        print("you win")
        break

