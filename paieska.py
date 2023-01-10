sakinys = "Studentai sėkmingai mokėsi su python ieškoti tekste sliekų..."
ieskom = input("ko ieškom?: ")
for raide in sakinys:
    if ieskom == raide:
        print("radom!")
        break
else:
    print(f"neradom {ieskom}.")
