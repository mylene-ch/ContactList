from tools import verify_email_address, verify_phone_numbers, get_contact_by_name
from storage import read_contacts, write_contacts


CONTACT_FILE_PATH = "contacts.json"


def add_contact(contacts):
    first_name = input("First Name: ").lower()
    last_name = input("Last Name: ").lower()
    mobile_num = input("Mobile Phone Number: ")
    home_num = input("Home Phone Number: ")
    email = input("Email Address: ")
    address = input("Address: ")

    if not first_name or not last_name:
        print("Contact must have a first and last name.")
    elif mobile_num and not verify_phone_numbers(mobile_num):
        print("Invalid mobile phone number.")
    elif home_num and not verify_phone_numbers(home_num):
        print("Invalid home phone number.")
    elif email and not verify_email_address(email):
        print("Invalid email address.")
    elif get_contact_by_name(first_name, last_name, contacts):
        print("A contact with this name already exists.")
    else:
        new_contact = {
            "first_name": first_name,
            "last_name": last_name,
            "mobile": mobile_num,
            "home": home_num,
            "email": email,
            "address": address
        }
        contacts.append(new_contact)
        print("Contact Added!")
        return
    print("You entered invalid information, this contact was not added.")


def search_for_contact(contacts):
    search_first_name = input("First Name: ").lower().strip()
    search_last_name = input("Last Name: ").lower().strip()

    matched_contacts = []
    for contact in contacts:
        first_name = contact["first_name"]
        last_name = contact["last_name"]
        if search_first_name and search_first_name not in first_name:
            continue
        if search_last_name and search_last_name not in last_name:
            continue

        matched_contacts.append(contact)

    print(f"Found {len(matched_contacts)} matching contacts.")
    list_contacts(matched_contacts)


def delete_contact(contacts):
    first_name = input("First Name: ").lower().strip()
    last_name = input("Last Name: ").lower().strip()

    contact = get_contact_by_name(first_name, last_name, contacts)
    if not contact:
        print("No contact with this name exists.")
    else:
        confirm = input(
            "Are you sure you would like to delete this contact (y/n)?").lower()
        if confirm == "y":
            contacts.remove(contact)
            print("Contact deleted.")


def get_contact_string(contact):
    string = f'{contact["first_name"].capitalize()} {contact["last_name"].capitalize()}'

    for field in ["mobile", "home", "email", "address"]:
        value = contact[field]
        if not value:
            continue
        string += f"\n\t{field.capitalize()}: {value}"

    return string


def list_contacts(contacts):
    sorted_contacts = sorted(contacts, key=lambda x: x["first_name"])

    for i, contact in enumerate(sorted_contacts):
        print(f"{i + 1}. {get_contact_string(contact)}")


def main(contacts_path):

    print("""Welcome to your contact list!

The following is a list of useable commands:      
"add": Adds a contact.
"delete": Deletes a contact.
"list": Lists all contacts.
"search": Searches for a contact by name.
"q": Quits the program and saves the contact list.
    """)

    contacts = read_contacts(contacts_path)

    while True:
        input_command = input("Type a command: ").lower().strip()

        if input_command == "add":
            add_contact(contacts)

        elif input_command == "delete":
            delete_contact(contacts)

        elif input_command == "list":
            list_contacts(contacts)

        elif input_command == "search":
            search_for_contact(contacts)

        elif input_command == "q":
            write_contacts(contacts_path, contacts)
            print("Contacts were saved successfully.")
            break


if __name__ == "__main__":
    main(CONTACT_FILE_PATH)
