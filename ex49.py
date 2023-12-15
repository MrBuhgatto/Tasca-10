#Importa el mòdul random i genera una llista de 20 elements aleatoris
from random import random
import random

#Funció per generar una llista de 20 elements aleatoris
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

#Funció per eliminar duplicats d'una llista
def elimina_duplicats(a):
    b = list(set(a))
    return b

#Programa principal: genera una llista, verifica duplicats i mostra la llista sense duplicats ordenada
x = llista_20_elements()
hi_ha_duplicats(x)
y = elimina_duplicats(x)
y.sort()
print("Llavors, la llista sense elements duplicats és {}".format(y))
