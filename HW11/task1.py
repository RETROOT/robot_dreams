phonebook = {}

def stats():
    print("Number of records:", len(phonebook))

def add():
    name = input("Input name: ")
    try:
        if name in phonebook:
            print("Error: entry with name", name, "already exists")
        else:
            lastname = input("Enter Lastname: ")
            phone = input("Enter a phone number: ")
            phonebook[name] = {'Phone number': phone, 'Lastname': lastname}
        print("The entry is added to the phone book")
    except Exception as e:
        print("Error:", str(e))

def delete(name):
    try:
        del phonebook[name]
        print("Entry by name", name, "deleted from phone book")
    except KeyError as e:
        print(f"Error: record with name {name} does not exist. Exc: {e}")
def show(name):
    try:
        record = phonebook[name]
        print(f"Name: {name}, Last name: {record['Lastname']}, Phone number: {record['Phone number']}")
    except KeyError as e:
        print(f"Error: record with name {name} does not exist. Exc: {e}")
def phonebook_list():
    for name in phonebook:
        print(name)

def help():
    print("Available commands:")
    print("stats - number of records")
    print("add - add a record")
    print("delete <name> - delete record by name (key)")
    print("list - list of all names in the book")
    print("show <name> - detailed information by name")
    print("help - list of available commands")
    print("quit - exit from the program")

def quit():
    print("Goodbye!")
    exit()

while True:
    command = input("Enter command: ")
    if command == "stats":
        stats()
    elif command == "add":
        add()
    elif command.startswith("delete "):
        name = command.split(" ")[1]
        delete(name)
    elif command == "list":
        phonebook_list()
    elif command.startswith("show "):
        name = command.split(" ")[1]
        show(name)
    elif command == "help":
        help()
    elif command == "quit":
        quit()
    else:
        print("Wrong command")