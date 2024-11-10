#tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

<<<<<<< HEAD
logger("aloitetaan ohjelma") #muutos mainissa

x = int(input("luku1: "))
y = int(input("luku2: "))
print(f"{x} + {y} = {summa(x, y)}") # muutos mainissa
print(f"{x} - {y} = {erotus(x, y)}") # muutos mainissa

logger("lopetetaan ohjelma")
print("goodbye!") #muutos bugikorjaus
