# kas_nors = input( "belekas ")
# kas = input( "anttras belekas ")
# print("košė " , kas + kas_nors)
# kas = "Labas"
# nors = "Rytas"
# ska = 5
# print("ska lygu: "+ str(ska) + " koks "+ kas + " grazus "+ nors)
import datetime
import calendar


class Sukaktis:
    def __init__(self, metai, menuo, diena, valandos, minutes):
        self.metai = metai
        self.menuo = menuo
        self.diena = diena
        self.valandos = valandos
        self.minutes = minutes
        self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)

    def smulkiai(self):
        now = datetime.datetime.now()
        skirtumas = now - self.data
        print(f"Praėjo metų: ", skirtumas.days // 365)
        print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
        print("Praėjo savaičių: ", skirtumas.days / 7)
        print("Praėjo dienų: ", skirtumas.days)
        print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
        print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
        print("Praėjo sekundžių: ", skirtumas.total_seconds())

    def arKeliamieji(self):
        if calendar.isleap(self.metai):
            print("Keliamieji metai")

    def atimtiDienas(self, dienos):
        return self.data - datetime.timedelta(days=dienos)

    def pridetiDienas(self, dienos):
        return self.data + datetime.timedelta(days=dienos)

    def __str__(self):
        return (
            f"Data: {self.metai}-{self.menuo}-{self.diena} {self.valandos}:{self.minutes}")


data1 = Sukaktis(1972, 3, 22, 0, 00)
data1.arKeliamieji()
data1.smulkiai()
print(data1.atimtiDienas(5))
print(data1.pridetiDienas(45))
print(data1)
