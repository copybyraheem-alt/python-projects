def run_bank():
    balance = 50

    while True:
        try:
            option = int(input("Choose an option (1: Balance, 2: Deposit, 3: Withdraw, 4: Quit): "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        match option:
            case 1:
                print(f"your balance is {balance}")
                
            case 2:
                try:
                    add = float(input("How much money you'd like to deposit: "))
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
                    continue
                if add <= 0:
                    print("Deposit amount must be positive!")
                else:
                    balance += add
                    print(f"{add} amount has been deposited into your account")
                    print(f"current balance {balance}")
                
            case 3:
                try:
                    sub = float(input("how much you wanna withdraw: "))
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
                    continue
                if sub <= 0:
                    print("Withdrawal amount must be positive!")
                elif sub > balance:
                    print("Insufficient funds!")
                else:
                    balance -= sub
                    print(f"you have withdrawn {sub} amount")
                    print(f"current balance {balance}")

            
            case 4:
                print("goodbye")
                break
            case _:
                print("invalid choice")

        again = input("choose again? (y/n): ").strip().lower()
        if again in ("n", "no"):
            break
                    
    return balance

if __name__ == "__main__":
    run_bank()
