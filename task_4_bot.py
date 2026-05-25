# Colors
RED = "\033[91m"
GREEN = "\033[92m"
GRAY = "\033[90m"
BLUE = "\033[94m"
RESET = "\033[0m"


def parse_input(user_input):
    parts = user_input.strip().split()

    if not parts:
        return "", []

    cmd = parts[0].lower()
    args = parts[1:]

    return cmd, args


def show_help():
    return f"""
{GRAY}
----------
Available commands:

hello                         - greeting
add [name] [phone]            - add new contact
change [name] [phone]         - change contact phone
phone [name]                  - show phone number
all                           - show all contacts
close or exit                 - exit the program
----------{RESET}
"""


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return f"\n{GREEN}Contact added.{RESET}"

    except ValueError:
        return f"\n{RED}Invalid command.{RESET}"


def change_contact(args, contacts):
    try:
        name, phone = args

        if name in contacts:
            contacts[name] = phone
            return f"\n{GREEN}Contact updated.{RESET}"

        return f"\n{RED}Contact not found.{RESET}"

    except ValueError:
        return f"\n{RED}Invalid command.{RESET}"


def show_phone(args, contacts):
    try:
        name = args[0]

        if name in contacts:
            return f"\n{GREEN}{contacts[name]}{RESET}"

        return f"\n{RED}Contact not found.{RESET}"

    except IndexError:
        return f"\n{RED}Invalid command.{RESET}"


def show_all(contacts):
    if not contacts:
        return f"\n{RED}No contacts saved.{RESET}"

    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return "\n" + result.strip()


def main():
    contacts = {}

    print(f"\n{BLUE}Welcome to the assistant bot!{RESET}")
    print(show_help())

    while True:
        user_input = input("\nEnter a command: ")

        if not user_input:
            print(f"\n{RED}Invalid command.{RESET}")
            print(show_help())
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(f"\n{BLUE}Good bye!{RESET}")
            break

        elif command == "hello":
            print(f"\n{GREEN}How can I help you?{RESET}")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print(f"\n{RED}Invalid command.{RESET}")

        print(show_help())


if __name__ == "__main__":
    main()