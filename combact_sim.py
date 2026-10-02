import random


def multi():
    multipliers = [1, 2, 3]
    return random.choice(multipliers)



def weapons():
    while True:
        choice = input("sword, bow, magic, (q) quit: ").strip().lower()

        damage = 0

        if choice == "sword":
            damage = 15
        elif choice == "bow":
            damage = 10
        elif choice == "magic":
            damage = 25
        elif choice == "q":
            print("bye")
            break
        else:
            print("Invalid choice, please select a valid weapon.")
            continue

        critical_multiplier = multi()
        total_damage = damage * critical_multiplier

        print(f"you used {choice}!, multiplier was {critical_multiplier} you delt {total_damage} damage")

        again = input("choose again? (y/n): ").strip().lower()
        if again == "n":
            break



if __name__=="__main__":
    weapons()