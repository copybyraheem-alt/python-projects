def items():
    item=['sword', 'shield', 'potion', 'armor']
    return item

def pricing(price):
    match price:
        case "sword":
            return 50
        case "shield":
            return 30
        case "potion":
            return 20
        case "armor":
            return 80
        case _:
            return None

gold= 100
inventory = []


while True:
    menu= input("1.view shop, 2.Buy item, 3. View inventory, 4. View gold, 5. Quit: ")

    if menu == "1":
        print(items())
    elif menu == "2":
        print(items())
        my_choice= input("choose your item: ").lower()
        cost= pricing(my_choice)
        if cost is None:
            print("Item not in shop!")
        elif gold >= cost:
            inventory.append(my_choice)
            print(f"you choose {my_choice} and the cost was {cost}")
            gold-=cost
            print(f"Total gold left: {gold}")
            print(f"Your inventory {inventory}")
        else:
            print("Insufficient gold!")
    elif menu == "3":
        print(f"Your inventory {inventory}")
    elif menu == "4":
        print(f"Total gold left: {gold}")
    elif menu == "5":
        print("byeee")
        break



