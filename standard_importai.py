import random
import math

skaicius = random.randint(1900, 2101)
print(skaicius, math.sqrt(skaicius))

from datetime import date
import calendar

print(f'ar keliamieji {skaicius}?: {calendar.isleap(skaicius)}')
print(f'siandien: {date.today()}')
