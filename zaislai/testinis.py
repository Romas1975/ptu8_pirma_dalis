from kiti_zaislai import geris

kintamasis = "Geras pirmadienio rytas"
# globalusis = "Testinis Pasauliukas"

def atbulai(stringas):
    # print(globalusis)
    return stringas[::-1]

print(f"Mano moduliukas {__name__} sėkmingai importuotas ir veikia")
print(geris.geras)

if __name__ == "__main__":
    print("testuojam:", kintamasis)
