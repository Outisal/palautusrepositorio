#tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan ohjelma")

x = int(input("luku1: "))
y = int(input("luku2: "))
print(f"Lukujen {x} ja {y} summa on {summa(x, y)}") # muutos bugikorjaus-branch
print(f"Lukujen {x} ja {y} erotus on {erotus(x, y)}") # muutos bugikorjaus-branch

logger("lopetetaan ohjelma")
print("goodbye!")
