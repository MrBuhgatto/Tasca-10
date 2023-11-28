###Definir una funció crear_punts() que agafi una llista de números i que pinti per pantalla tants punts com el valor de cada número de la llista. Entre els elements de la llista, hi ha d’haver un salt de línia. Ex: crear_punts([2,3,4]) mostri per pantalla el següent:
#..
#...
#....
"""def llegir_llista():
    a= 'o'
    l=[]
    while a!='.':
        a=input("Introdueix una llista: ")
        if a == '.':
            l.append(int(a))
        else:
            return l
        
def crear_punts():
    a='.'
    b=llegir_llista()
    c=b
    for a in c:
        print(c * '.')
    return a[::-1]   
print(crear_punts())
l=llegir_llista()"""


def crear_puntos(l):
    for n in l:
        print("." * n)

#Program principal
crear_puntos([1, 2, 3])