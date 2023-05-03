import json
import re
import datetime

filename = 'phoonebook.json'

def validate_phone_number(number):
#    pattern = r'^(?:\+?38|0)?\d{9,10}$'
    pattern = '^(?:\+?38)?0\d{9}$'
    return bool(re.match(pattern, number))
class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("error.log", "a") as f:
            f.write(f"Error at {self.timestamp}: {self.message}\n")
        super().__init__(self.message)
def log_time(func):
    def wrapper(*args, **kwargs):
        with open('log.txt', 'a') as f:
            current_time = datetime.datetime.now()
            function_name = func.__name__
            f.write(f"{function_name} was called at {current_time}\n")
        return func(*args, **kwargs)
    return wrapper
def create_file():
    with open(filename, 'w') as f:
        json.dump({}, f)
    print(f"The file [filename] has been created.")

def save_phonebook():
    with open(filename, 'w') as f:
        json.dump(phonebook, f)
#        print("The phonebook has been saved to the file.")
def load_phoonebook():
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        create_file()
        return {}
phonebook = load_phoonebook()

@log_time
def stats():
    print("Number of records:", len(phonebook))
@log_time
def add():
    name = input("Input name: ")
    try:
        if name in phonebook:
            print("Error: entry with name", name, "already exists")
        else:
            lastname = input("Enter Lastname: ")
            phone = input("Enter a phone number: ")
            phonebook[name] = {'Phone number': phone, 'Lastname': lastname}
            if validate_phone_number(phone):
                phonebook[name] = {'Phone number': phone, 'Lastname': lastname}
                save_phonebook()
                print("The entry is added to the phone book")
            else:
                print("Error: Invalid phone number format")
                while True:
                    phone = input("Enter a valid phone number: ")
                    if validate_phone_number(phone):
                        phonebook[name] = {'Phone number': phone, 'Lastname': lastname}
                        save_phonebook()
                        print("The entry is added to the phone book")
                        break
                    else:
                        print("Error: Invalid phone number format, try again")
    except Exception as e:
        print("Error:", str(e))
@log_time
def delete(name):
    try:
        del phonebook[name]
        save_phonebook()
        print("Entry by name", name, "deleted from phone book")
    except KeyError as e:
        print(f"Error: record with name {name} does not exist. Exc: {e}")
    except CustomException as e:
        print("An error was received, check error.log")
@log_time
def show(name):
    try:
        record = phonebook[name]
        print(f"Name: {name}, Last name: {record['Lastname']}, Phone number: {record['Phone number']}")
    except KeyError as e:
        print(f"Error: record with name {name} does not exist. Exc: {e}")
    except CustomException as e:
        print("An error was received, check error.log")
@log_time
def phonebook_list():
    for name in phonebook:
        print(name)
@log_time
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