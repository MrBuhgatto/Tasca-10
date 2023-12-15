#Importa el mòdul random i genera una llista de 20 elements aleatoris
from random import random
import random

def llista_20_elements():
    l = []
    for i in range(20):
        l.append(random.randint(1, 100))
    return l

#Funció per verificar si hi ha elements duplicats en una llista
def hi_ha_duplicats(a):
    seen = set()
    dupes = [x for x in a if x in seen or seen.add(x)]
    if len(dupes) > 0:
        print("La llista {} té elements duplicats {}".format(a, dupes))
    else:
        print("La llista {} no té elements duplicats {}".format(a, dupes))

#Programa principal: genera una llista i verifica si té elements duplicats
x = llista_20_elements()
hi_ha_duplicats(x)
