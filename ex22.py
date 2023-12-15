###Definir una funció crear_punts() que agafi una llista de números i que pinti per pantalla tants punts com el valor de cada número de la llista. Entre els elements de la llista, hi ha d’haver un salt de línia. Ex: crear_punts([2,3,4]) mostri per pantalla el següent:
#..
#...
#....
#Funció que crea una cadena repetint un caràcter un cert nombre de vegades
def crear_repetits(a, b):
    c = b * int(a)
    return c

#Funció que crea una seqüència de punts basada en una llista numèrica
def crear_punts(a):
    for e in a:
        c = crear_repetits(int(e), '.')
        print(c)

#Entrada de l'usuari i crida a la funció
a = input("Escriu una llista numèrica d'elements separats per comes: ")
crear_punts(a)
