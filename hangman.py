def play_hangman(secret_word="apple"):
    health = 6
    display = ["_"] * len(secret_word)
    guessed_letters = set()

    print("-----------HANGMAN----------")
    print(f"guess: {' '.join(display)}")
    print(f"your health: {health}")

    while True:
        guess = input("guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter (a-z)!")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'! Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            for position, letter in enumerate(secret_word):
                if letter == guess:
                    display[position] = guess
        else:
            health -= 1
            print("Wrong guess!")

        print(f"your current health is: {health}")
        print(f"guess: {' '.join(display)}")
        print("---------------------")

        if health <= 0:
            print("Game-over!, you died")
            print(f"The word was: {secret_word}")
            break

        if "_" not in display:
            print("you win")
            break


if __name__ == "__main__":
    play_hangman()
