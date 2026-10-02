import random


def scan_file():
    scanner = ["safe", "malware", "phishing"]
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
        case _:
            return 0

def run_firewall():
    health = 100

    while True:
        run = input("Press Enter to scan, or 's' to exit: ").strip().lower()

        if run == "s":
            print("byeeee")
            break

        caught_data = scan_file()
        damage = calculate_damage(caught_data)

        health = max(0, health - damage)

        print(f"File was: {caught_data}. it did {damage} damage ")
        print(f"current health: {health}")

        if health <= 0:
            print("Firewall breached! System offline.")
            break
        
if __name__=="__main__":

    run_firewall()