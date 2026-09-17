def multi():
      import random

      Critical_Multiplier = [1, 2, 3,]
      random_ch = random.choice(Critical_Multiplier)

      return random_ch



def weapons():
    while True:
        choice = input("sword, bow, magic, (q) quit: ").lower()

        damage=0
        
    
        if choice == "sword":
                damage +=15

        elif choice == "bow":
                damage +=10

        elif choice== "magic":
                damage +=25
        else:
                print("bye")
                break


        Critical_Multiplier= multi()

        
        damage *=Critical_Multiplier

        print(f"you used {choice}!, multiplier was {Critical_Multiplier} you delt {damage} damage")



        again = input("choose again/ (y/n)")
        if again == "n":
            break



if __name__=='__main__':
    weapons()