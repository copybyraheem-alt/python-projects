while True:
    print(("1.add 2.sub 3.multi 4.div 5.sqare 6.table 7.even/odd 8. prime 9. exit"))
    chose=input("Choose one of this: ")

    match chose:
        case "9":
            print("byeee")
            break
        case "1":
            num1=int(input("Enter number 1: "))
            num2=int(input("Enter number2:  "))
            total=num1 +num2
            print (f"The answer is {total}")
            break
        case "2":
            num3=int(input("Enter number 1: "))
            num4=int(input("Enter number 2: "))
            total2= num3-num4
            print(f"The answer is {total2}")
            break
        case "3":
            num5=int(input("Enter number 1: "))
            num6=int(input("Enter number2: "))
            total3= num5 *num6
            print(f"The answer is: {total3}")
            break
        case "4":
            num7=int(input("Enter number 1: "))
            num8=int(input("Enter number2: "))
            total4=num7/num8
            print(f"The answer is : {total4}")
            break

        case "5":
            num9=int(input("Enter number 1: "))
            total5= num9 *num9
            print(f"The answer is: {total5}")
            break

        case "6":
            num=int(input("Enter a number you want the table for: "))
            for i in range(1, 11):
                print(f"{i} * {num}= {i*num}")
                
        case "7":
            num11=int(input("Enter number 1: "))
            if num11%2==0:
                print("it is even")
                break
            else:
                print("it is odd")
                break
        case "8":
            primenum=int(input("Enter your number: "))
            prime_check= True
            if primenum<=1:
                prime_check=False
            else:
                for i in range(2, primenum):
                    if primenum%i==0:
                        prime_check=False
            if prime_check ==True:
                print("---------------------")
                print("Your number is prime")
                print("---------------------")
                break
            else:
                print("---------------------")
                print("Your number is not prime")
                print("Your number is not prime")
                print("---------------------")
                

        case _:
            print("sleep")
            break