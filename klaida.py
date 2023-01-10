skaicius = input("iveskite skaiciu: ")
try:
    tiesa = int(skaicius) > 0
except Exception as error:
    print("klaida:", error)
else:
    print(f"{skaicius} yra daugiau už 0: {tiesa}")
