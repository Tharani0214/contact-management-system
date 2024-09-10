import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email, address):
    contacts = load_contacts()
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

def display_contacts():
    contacts = load_contacts()
    if contacts:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
    else:
        print("No contacts found.")

def search_contact(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found contact: {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
            return
    print("Contact not found.")

def delete_contact(name):
    contacts = load_contacts()
    new_contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def menu():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    menu()
