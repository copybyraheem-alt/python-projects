def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    while True:
        print("\n1.add 2.sub 3.multi 4.div 5.square 6.table 7.even/odd 8.prime 9.exit")
        choice = input("Choose one of these: ").strip()

        match choice:
            case "9":
                print("byeee")
                break
            case "1":
                num1 = get_int("Enter number 1: ")
                num2 = get_int("Enter number 2: ")
                total = num1 + num2
                print(f"The answer is {total}")
            case "2":
                num3 = get_int("Enter number 1: ")
                num4 = get_int("Enter number 2: ")
                total2 = num3 - num4
                print(f"The answer is {total2}")
            case "3":
                num5 = get_int("Enter number 1: ")
                num6 = get_int("Enter number 2: ")
                total3 = num5 * num6
                print(f"The answer is: {total3}")
            case "4":
                num7 = get_int("Enter number 1: ")
                num8 = get_int("Enter number 2: ")
                if num8 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    total4 = num7 / num8
                    print(f"The answer is : {total4}")
            case "5":
                num9 = get_int("Enter number 1: ")
                total5 = num9 * num9
                print(f"The answer is: {total5}")
            case "6":
                num = get_int("Enter a number you want the table for: ")
                for i in range(1, 11):
                    print(f"{i} * {num}= {i*num}")
            case "7":
                num11 = get_int("Enter number 1: ")
                if num11 % 2 == 0:
                    print("it is even")
                else:
                    print("it is odd")
            case "8":
                primenum = get_int("Enter your number: ")
                prime_check = True
                if primenum <= 1:
                    prime_check = False
                else:
                    for i in range(2, int(primenum**0.5) + 1):
                        if primenum % i == 0:
                            prime_check = False
                            break
                if prime_check:
                    print("---------------------")
                    print("Your number is prime")
                    print("---------------------")
                else:
                    print("---------------------")
                    print("Your number is not prime")
                    print("---------------------")
            case _:
                print("Invalid choice, please select an option from 1 to 9.")


if __name__ == "__main__":
    main()
