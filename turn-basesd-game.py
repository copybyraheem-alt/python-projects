import random


def computer():
    moves= ['kick', 'punch', 'gun', 'knife']
    choice = random.choice(moves)
    return choice

def damage(something):
    if something == "kick":
        return 50
    elif something == "punch":
        return 30
    elif something == "gun":
        return 100
    elif something == "knife":
        return 80
    else:
        return 0

my_health = 500
com_health = 500

turn = 0
while True:
    my_try= input("kick, punch, gun, knife?, choose: ").lower()

    my_damage = damage(my_try)
    

    com_movee=computer()
    com_damage= damage(com_movee)
    print("----------------------------------------------")
    print(f"The computer choose {com_movee} and delt {com_damage} damage")
    print(f"You choose {my_try} and delt {my_damage}")

    my_health -= com_damage
    com_health -= my_damage

    print("--------------------HEALTH-------------------------")
    print(f"your current health {my_health}")
    print(f"Computer's current {com_health}")
    print("----------------------------------------------------")
    turn += 1
    print(f"This was round {turn}")

    if com_health <= 0:
        print("youu winnnnnn")
        won_level_1 = True
        break
    elif my_health <= 0:
        print("you lose")
        won_level_1 = False
        break



def boss_attack():
    boss_moves = ["strike", "gun", "laser", "kick", "throw"]
    return random.choice(boss_moves)


def boss_damage(attack_name):
    match attack_name:
        case "strike":
            return 150
        case "gun":
            return 100
        case "laser":
            return 200
        case "kick":
            return 50
        case "throw":
            return 120
        case _:
            return 0


if won_level_1:
    level_2 = input("Want to jump into level 2 (y/n): ").lower()
else:
    level_2 = "n"

print()
round = 1
lvl_2_health = 500
boss_health = 300

while True:
    if level_2 == "n":
        break

    if round == 1:
        print("-------Get ready for a adventure my friend-------------")
        print("you wont a weapon here, in order to defeat him you have to dodge him until he is tired")
        print("who is him?, you'll know pretty soon :)")
        print()
    round += 1

    dodge_num = random.randint(1, 10)
    player_dodge = int(input("guess the number to dodge: "))

    boss_att = boss_attack()
    boss_dam = boss_damage(boss_att)

    print("-------------------------------")
    if player_dodge == dodge_num:
        print("you dodged it, yay!!!")
        dodge_damage = [20, 30, 50, 5000]
        picked_damage = random.choice(dodge_damage)
        boss_health -= picked_damage 
        print(f"You delt {picked_damage} damage")
        print(f"The boss health is {boss_health}")
    else:
        lvl_2_health -= boss_dam
        print("wrong guess, you were not able to dodge it")
        print(f"your current health {lvl_2_health}")
        print(f"The boss used {boss_att} and delt you {boss_dam} damage")
        print(f"Boss's current health {boss_health}")
    print("-------------------------------")

    if lvl_2_health <= 0:
        print("You lostt")
        print("Game over!")
        print("----------------")
        break
    elif boss_health <= 0:
        print("You wonnnnn")
        print("Game over!")
        print("----------------")
        break






