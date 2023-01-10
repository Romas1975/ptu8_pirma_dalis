import datetime

data = datetime.datetime.strptime(input('iveskite data "metai" "Menuo" "diena" formatu: '), "%Y %B %d")
# print(type(data))
print(f"ivesta data: {data.strftime('%A, %B %d, %Y')}")
siandien = datetime.date.today()
print(f"siandien: {siandien.strftime('%A, %B %d, %Y')}")
amzius = siandien - data.date()
print(f"nuo ivestos datos praejo {amzius.days} dienu")
