import os, pickle

CATALOG_FILE = 'media/catalog.pkl'
catalog = []
message = None

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_message():
    global message
    if message:
        print('_'*(len(message)+4))
        print(f"| {message} |\n")
    message = None

def print_menu():
    print("===[ MENU ]===")
    print("1| new catalog")
    print("2| save file")
    print("3| load file")
    print("4| create entry")
    print("5| read entries")
    print("6| edit entry")
    print("7| delete entry")
    print("0| X, or nothing for exit")

def create_entry():
    global message
    print("===[4| CREATE ENTRY ]===")
    person = {
        "first name": input("First name: "),
        "last name": input("Last name: "),
    }
    catalog.append(person)
    message = f"Successfully created {person['first name']} {person['last name']}"
    return catalog

def print_catalog():
    print("===[5| PERSONS LIST ]===")
    if not len(catalog) > 0:
        print("Catalog is empty...")
    for id, person in enumerate(catalog):
        print(f"ID: {id}, {person['first name']} {person['last name']}")
    input("...just ENTER to continue...")

def save_catalog():
    global message
    try:
        with open(CATALOG_FILE, 'wb') as pkl:
            pickle.dump(catalog, pkl)
    except Exception as error:
        message = f"ERROR: saving to {CATALOG_FILE} FAILED! Reason: {error}!"
    else:
        message = f"Catalog successfully saved to {CATALOG_FILE}"

def load_catalog():
    global message
    try:
        with open(CATALOG_FILE, 'rb') as pkl:
            catalog = pickle.load(pkl)
    except:
        message = f"ERROR: loading from {CATALOG_FILE} FAILED!"
        return []
    else:
        message = f"Catalog succesfully loaded from {CATALOG_FILE}"
        return catalog

def delete_entry():
    global message
    print("===[7| DELETING PERSON ]===")
    try:
        id = int(input("Enter person ID: "))
        deleted = catalog.pop(id)
    except ValueError:
        message = f"ERROR: Wrong ID format, must be a number."
    except IndexError:
        message = f"ERROR: Person with ID:{id} does not exist."
    else:
        message = f"{deleted['first name']} {deleted['last name']} was succesfully deleted."
    finally:
        return catalog


while True:
    clear()
    print_message()
    print_menu()
    choice = input('Make a choice: ')
    clear()
    if choice.lower() == "x" or choice == "0" or choice == "":
        break
    if choice == "1":
        catalog = []
        message = "Catalog is now empty..."
    if choice == "2":
        save_catalog()
    if choice == "3":
        catalog = load_catalog()
    if choice == "4":
        catalog = create_entry()
    if choice == "5":
        print_catalog()
    if choice == "7":
        catalog = delete_entry()
