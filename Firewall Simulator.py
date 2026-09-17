def scan_file():
    import random
    scanner =["safe", "malware", "phishing"]
    result = random.choice(scanner)

    return result


def calculate_damage(file_type):

    match file_type:
        case "safe":
            return 0
        case "malware":
            return 20
        case "phishing":
            return 10

    return file_type

def run_firewall():
    health = 100

    while True:
        run = input("Press Enter for result, or 's' to exit: ")

        if run == "s":
            print("byeeee")
            break
        

        caught_data= scan_file()
        damage = calculate_damage(caught_data)

        health -= damage

        print(f"File was: {caught_data}. it did {damage} damage ")
        print(f"current health: {health}")


        again= input("choose again? (y/n)")
        if again == "n":
            break
        
if __name__=="__main__":

    run_firewall()