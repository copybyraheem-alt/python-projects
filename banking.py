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
                    add = int(input("How much money you'd like to deposit: "))
                except ValueError:
                    print("Invalid amount! Please enter a valid number.")
                    continue
                if add <= 0:
                    print("Deposit amount must be positive!")
                else:
                    balance += add
                    print(f"{add} amount has been depoisted into your account")
                    print(f"current balance {balance}")
                
            case 3:
                try:
                    sub = int(input("how much you wanna withdraw: "))
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
                print("invaild choice")

        again= input("choose again? (y/n): ")
        if again.lower() == "n":
            break
                    
    return option

if __name__ == "__main__":
    run_bank()