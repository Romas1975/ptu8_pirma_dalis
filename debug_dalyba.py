import logging
from datetime import date

siandien = date.today()
# logging.basicConfig(
#     level=logging.DEBUG, 
#     filename=f'logs/debug_dalyba_{siandien.strftime("%Y%m%d")}.log',
#     format="%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(message)s",
# )
logger = logging.getLogger(__name__)
logo_failas = logging.FileHandler(f'logs/debug_dalyba_{siandien.strftime("%Y%m%d")}.log')
logger.addHandler(logo_failas)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(funcName)s:%(message)s")
logo_failas.setFormatter(formatter)

def dalyba(a, b):
    padalinom = a / b
    # print(f"{a} / {b} = {padalinom}")
    logger.critical(f'vykdant funkcija {dalyba.__name__} buvo {a} padalinta is {b} ir gauta {padalinom}')
    return padalinom

print(dalyba(22, 5))
print(dalyba(15, 5))
print(dalyba(0.5, 5))
