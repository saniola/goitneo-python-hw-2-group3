import re

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return "Error: Invalid number of arguments. Use 'add [name] [phone number]'."
            elif func.__name__ == "change_contact":
                return "Error: Invalid number of arguments. Use 'change [name] [new phone number]."
            elif func.__name__ == "show_phone":
                return "Error: Invalid number of arguments. Use 'phone [name]'."
            elif func.__name__ == "show_all":
                return "Error: Use 'all' without arguments."
        except KeyError:
            if func.__name__ == "show_phone" or func.__name__ == "change_contact":
                name = args[0]
                return f"Error: Contact with name {name} not found."
            if func.__name__ == "show_all":
                return "Error: The contacts list is empty."
        except TypeError:
            if func.__name__ == "change_contact" or func.__name__ == "add_contact":
                return "Error: The phone number must be 10 digits"
    return inner

def is_valid_phone(phone):
    pattern = r'^\d{10}$'

    if re.match(pattern, phone):
        return True
    else:
        return False

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, args

@input_error
def add_contact(args, contacts):
    name, phone = args
    name = name.lower()

    if not is_valid_phone(phone):
        raise TypeError

    contacts[name] = phone

    return f"Contact {name} with phone number {phone} added."

@input_error
def change_contact(args, contacts):
    name, new_phone = args
    name = name.lower()

    if not is_valid_phone(new_phone):
        raise TypeError

    if name in contacts:
        contacts[name] = new_phone

        return f"Contact {name} updated. New phone number: {new_phone}."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    name = args[0]
    name = name.lower()

    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}."
    else:
        raise KeyError

@input_error
def show_all(args, contacts):
    if len(args) > 0:
        raise ValueError

    if not contacts:
        raise KeyError

    if len(contacts) > 0:
        result = "All saved contacts with phone numbers:\n"

        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result

def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")

            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()
