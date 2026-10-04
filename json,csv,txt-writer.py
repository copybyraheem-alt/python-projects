import json
import csv


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        if not isinstance(name, str) or not isinstance(phone, str) or not isinstance(email, str):
            return False
        name = name.strip()
        phone = phone.strip()
        email = email.strip()
        if not name or not phone or not email:
            return False
        self.contacts.append({"name": name, "phone": phone, "email": email})
        return True

    def save_txt(self, file_path):
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("Contacts\n")
                for contact in self.contacts:
                    file.write(f"{contact['name']} | {contact['phone']} | {contact['email']}\n")
            return True
        except OSError:
            return False

    def save_json(self, file_path):
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(self.contacts, file, indent=4)
            return True
        except OSError:
            return False

    def save_csv(self, file_path):
        try:
            with open(file_path, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "phone", "email"])
                for contact in self.contacts:
                    writer.writerow([contact['name'], contact['phone'], contact['email']])
            return True
        except OSError:
            return False


def main():
    book = ContactBook()
    result = book.add_contact("dude", "5864648", "asdb2gmail.com")
    if not result:
        print("Setup error: invalid contact.")
        return
    if book.save_txt("contacts.txt"):
        print("TXT saved")
    else:
        print("TXT failed")

    if book.save_json("contacts.json"):
        print("JSON saved")
    else:
        print("JSON failed")

    if book.save_csv("contacts.csv"):
        print("CSV saved")
    else:
        print("CSV failed")


if __name__ == '__main__':
    main()
