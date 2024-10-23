def hello():
    return "How can I help you?"

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Error: Please provide both a username and a phone number."

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone  
            return f"Contact {name} updated."
        else:
            return f"Error: Contact {name} not found."
    except ValueError:
        return "Error: Please provide both a username and a phone number."

def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return f"Error: Contact {name} not found."

def show_all_contacts(contacts):
    if contacts:
        return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    contacts = {}

    while True:
        user_input = input("Enter command: ").strip().lower() 
        command, *args = user_input.split()

        if command == "hello":
            print(hello())

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(get_phone(args, contacts))

        elif command == "all":
            print(show_all_contacts(contacts))

        elif command in ["close", "exit"]:
            print("Good bye!")
            break

        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()