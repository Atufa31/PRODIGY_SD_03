import json

contacts = []

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    
    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email
    }
    
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"Contact {idx}:")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print()


def edit_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        contact_idx = int(input("Enter the contact number you want to edit: ")) - 1
        if 0 <= contact_idx < len(contacts):
            contact = contacts[contact_idx]
            print("Editing Contact:")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            
            contact["Name"] = input("Enter the new name (leave empty to keep current): ") or contact["Name"]
            contact["Phone"] = input("Enter the new phone number (leave empty to keep current): ") or contact["Phone"]
            contact["Email"] = input("Enter the new email address (leave empty to keep current): ") or contact["Email"]
            
            print("Contact edited successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        contact_idx = int(input("Enter the contact number you want to delete: ")) - 1
        if 0 <= contact_idx < len(contacts):
            deleted_contact = contacts.pop(contact_idx)
            print(f"Contact '{deleted_contact['Name']}' deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid contact number.")

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contacts saved to 'contacts.json'.")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
        print("Contacts loaded from 'contacts.json'.")
    except FileNotFoundError:
        print("No saved contacts found.")

while True:
    print("\nContact Manager Menu:")
    print("1. Add a new contact")
    print("2. View contacts")
    print("3. Edit a contact")
    print("4. Delete a contact")
    print("5. Save contacts")
    print("6. Load contacts")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        save_contacts()
    elif choice == "6":
        load_contacts()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
