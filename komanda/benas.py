import random

vardas = input("Iveskite savo varda: ")
print(f"Sveiki atvyke i mano zaidima, {vardas}!")

skaicius = random.randint(1, 10)
spejimu_kiekis = 0
while True:
    try:
        spejimas = int(input("spekit skaiciu nuo 1 iki 10: "))
        spejimu_kiekis += 1
    except ValueError:
        print('Ivedete ne skaiciu, bandykit per naujo')
    else:
        if skaicius != spejimas:
            if spejimas > skaicius:
                print("Bandykite mazesni skaiciu")
            else:
                print("Bandykite didesni skaiciu")

        if skaicius == spejimas:
            print(f"Puiku! teisingas skaicius buvo {skaicius}")
            print(f"Sveikinu {vardas} jus laimejote, atspejote is {spejimu_kiekis} kartu!")
            break