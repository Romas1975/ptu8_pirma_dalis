import logging
from datetime import date

# import debug_dalyba # kadangi debug dalyba irgi turi logging, jie pykstasi

siandien = date.today()
# logging.basicConfig(
#     level=logging.INFO, 
#     filename=f'logs/debug_kates_{siandien.strftime("%Y%m%d")}.log',
#     format="%(asctime)s:%(levelname)s:%(funcName)s:%(message)s",
# )
logger = logging.getLogger(__name__)
logo_failas = logging.FileHandler(f'logs/debug_kates_{siandien.strftime("%Y%m%d")}.log')
logger.addHandler(logo_failas)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(message)s")
logo_failas.setFormatter(formatter)
terminalas = logging.StreamHandler()
terminalas.setFormatter(formatter)
logger.addHandler(terminalas)


class Kate:
    vardas = ""
    spalva = ""
    kojos = 0
    amzius = 0

    def __init__(self, vardas, spalva="juoda", kojos=4):
        if len(vardas) > 0:
            self.vardas = vardas
        else:
            raise ValueError("Klaida: vardas turi buti ivestas")
        self.spalva = spalva
        self.kojos = kojos
        self.amzius = 0
        logger.info(f'Sukurta kate {self}')

    def miaukseti(self):
        print("miau")

    def _judinti_kojas(self, kaip=""):
        return kaip

    def _ziureti(self, kur="tiesiai"):
        return kur

    def begti(self, kryptis="tiesiai", judesys=""):
        kaip = self._judinti_kojas(judesys)
        kur = self._ziureti(kryptis)
        if kaip:
            print(f"begu {kaip} {kur}")
        else:
            print(f"begu {kur}")

    def susilauzyti_koja(self, kiek=1):
        self.kojos -= kiek
        logger.error(f'{self} susilauze koja')

    def sugydyti_koja(self, kiek=1):
        self.kojos += kiek
        logger.warning(f'{self} susigyde koja')

    def __str__(self) -> str:
        return f"vardas: {self.vardas}, spalva: {self.spalva}, kojos: {self.kojos}, amzius: {self.amzius}"

    def __repr__(self) -> str:
        return f"({self.vardas}, {self.spalva}, {self.kojos})"


if __name__ == "__main__":
    kates = []
    while True:
        print("===[ KATINYNAS ]===")
        print("1 | prideti kate")
        print("2 | rodyti kates")
        print("7 | prideti/gydyti koja")
        print("8 | lauzyti/atimti koja")
        print("9 | palaidoti kate")
        print("0 | padeti rageli")
        try:
            pasirinkimas = int(input("Pasirinkite:"))
            logger.debug(f'pasirinkta: {pasirinkimas}')
        except ValueError:
            print("blogas pasirinkimas, bandykite dar")
        else:
            if pasirinkimas == 0:
                break
            if pasirinkimas == 1:
                try:
                    nauja = Kate(
                        input("Vardas: "),
                        input("Spalva: ") or "Juodas",
                        int(input("Kojos: ") or 4),
                    )
                except ValueError as error:
                    logger.error(f"Klaida: {error}")
                    print(f"Klaida: {error}")
                else:
                    kates.append(nauja)
                    print(f"Gime nauja kate {nauja}")
            if pasirinkimas == 2:
                if len(kates):
                    for id, kate in enumerate(kates):
                        print(f"ID: {id}, {kate}")
                else:
                    print('Kolkas kaciu nera...')
            if pasirinkimas == 7:
                try:
                    id = int(input("Iveskite kates ID: "))
                    kates[id].sugydyti_koja()
                except ValueError as error:
                    logger.error(f"Klaida: {error}")
                    print("Klaida: ID turi buti skaicius")
                except IndexError as error:
                    logger.error(f"Klaida: {error}")
                    print("Klaida: Kate su tokiu ID neegzistuoja")
                else:
                    print(f"Kate: {kates[id]}")
            if pasirinkimas == 8:
                try:
                    id = int(input("Iveskite kates ID: "))
                    kates[id].susilauzyti_koja()
                except ValueError as error:
                    logger.error(f"Klaida: {error}")
                    print("Klaida: ID turi buti skaicius")
                except IndexError as error:
                    logger.error(f"Klaida: {error}")
                    print("Klaida: Kate su tokiu ID neegzistuoja")
                else:
                    print(f"Kate: {kates[id]}")
            if pasirinkimas == 9:
                try:
                    id = int(input("Iveskite kates ID, kuria trinam: "))
                    palaidota = kates.pop(id)
                except ValueError as error:
                    logger.error(f"Klaida: {error}")
                    print("Klaida: ID turi buti skaicius")
                except IndexError as error:
                    logger.error(f"Klaida: {error}")
                    print("Klaida: Kate su tokiu ID neegzistuoja")
                else:
                    print(f"Kate {palaidota} buvo palaidota")
