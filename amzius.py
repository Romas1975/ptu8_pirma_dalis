import datetime

metai = input('iveskite metus: ')
menuo = input('iveskite menesi: ')
diena = input('iveskite diena: ')

data = datetime.datetime.strptime(f"{metai}-{menuo}-{diena}", "%Y-%m-%d")
print(type(data))
print(f"ivesta data: {data.strftime('%A, %B %d, %Y')}")
siandien = datetime.date.today()
print(f"siandien: {siandien.strftime('%A, %B %d, %Y')}")
amzius = siandien - data.date()
print(f"nuo ivestos datos praejo {amzius.days} dienu")
