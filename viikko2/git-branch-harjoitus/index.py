#tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus
from tulo import tulo
from osamaara import osamaara

logger("aloitetaan ohjelma") #muutos mainissa

x = int(input("luku1: "))
y = int(input("luku2: "))
print(f"{x} + {y} = {summa(x, y)}") # muutos mainissa
print(f"{x} - {y} = {erotus(x, y)}") # muutos mainissa
print(f"{x} * {y} = {tulo(x, y)}")
print(f"{x} / {y} = {osamaara(x, y)}")

logger("lopetetaan ohjelma")
print("goodbye!") #muutos bugikorjaus
