def print_name(name):
    print(f"Sveiki, {name}!")

while True:
    user_input = input("Koks jusu vardas? ")
    if user_input != "":
        print_name(user_input)
    elif user_input == "":
        print("Neparasete vardo, programa uzdaroma.")
        break