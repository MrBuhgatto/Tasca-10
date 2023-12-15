###Definir una funció sumar_llista() i una funció multiplicar_llista() que sumin i multipliqueu, respectivament, tots els valors d’una llista. 
###Prova-la amb diferents exemples. Ex: sumar_llista([1,2,3,4]) retorni 10.
#Funció per sumar els elements d'una llista
def sumar_llista(a):
    suma = 0
    for i in a:
        suma += i
    return suma

#Funció per multiplicar els elements d'una llista
def multiplicar_llista(a):
    multiplicar = 1
    for i in a:
        multiplicar *= i
    return multiplicar

#Ús de les funcions:
x = [3, 4, 5, 7]
print("La suma de tots els elements de la llista és: ", sumar_llista(x))
print("La multiplicació de tots els elements de la llista és: ", multiplicar_llista(x))
