def items():
    item=['sword', 'shield', 'potion', 'armor']
    return item

def pricing(price):
    match price:
        case "sword":
            return 50
        case "sheld":
            return 30
        case "potion":
            return 20
        case "armor":
            return 80

gold= 100
inventory = []


while True:
    menu= input("1.view shop, 2.Buy item, 3. View inventory, 4. View gold, 5. Quit: ")
    cost= pricing(my_choice)



    if menu == "1":
        print(items())
    elif menu == "2":
        print(items())
        my_choice= input("choose your item: ")
        if gold < cost:
            inventory.append(my_choice)
            cost= pricing(my_choice)
            print(f"you choose {my_choice} and the cost was {cost}")
            gold-=cost
            print(f"Total gold left: {gold}")
            print(f"Your inventory {inventory}")
    elif menu == "3":
        print(f"Your inventory {inventory}")
    elif menu == "4":
        print(f"Total gold left: {gold}")
    elif menu == "5":
        print("byeee")
        break



