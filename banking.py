def run_bank():
    balance = 50

    while True:
        option = int(input("Choose an option (1: Balance, 2: Deposit, 3: Withdraw, 4: Quit: "))

        match option:
            case 1:
                f"your balance is {balance}"
                print(f"your balance is {balance}")
                
            case 2:
                add= int(input(f"How much money you'd like to deposit: "))
                balance +=add
                print(f"{add} amount has been depoisted into your account")
                print(f"current balance {balance}")
                
            case 3:
                sub= int(input("how much you wanna withdraw: "))
                if sub > balance:
                    print("Insufficient funds!")
                    break
                    
                balance -= sub
                print(f"you have withdrawn {sub} amount")
                print(f"current balance {balance}")

            
            case 4:
                print("goodbye")
                break
            case _:
                print("invaild choice")

        again= input("choose again? (y/n)")
        if again == "n":
            break
                    
    return option

if __name__ == "__main__":
    run_bank()