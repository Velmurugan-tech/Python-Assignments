import json

FILE = "contacts.json"

def load_contacts():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    save_contacts(contacts)

def show_contacts(contacts):
    for name, phone in contacts.items():
        print(name, phone)

contacts = load_contacts()

while True:
    print("1.Add 2.Show 3.Exit")
    choice = input("Choice: ")
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        show_contacts(contacts)
    else:
        break
