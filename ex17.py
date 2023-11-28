###Definir una funció sumar_llista() i una funció multiplicar_llista() que sumin i multipliqueu, respectivament, tots els valors d’una llista. 
###Prova-la amb diferents exemples. Ex: sumar_llista([1,2,3,4]) retorni 10.

"""def llegir_llista():
    a= 'o'
    l=[]
    while a!='.':
        a=input("Introdueix una llista: ")
        if a == '.':
            l.append(int(a))
        else:
            return l
def sumar_llista(l):
    s=0
    for e in l:
        s+=e
        print('La suma de tots els elements de la llista {} és {}'.format(l,s))
def sumar_llista():
    s=0
    for e in l:
        s*=e
        print('El producte de tots els elements de la llista {} és {}'.format(l,s))


#Programa principal
l = llegir_llista()
sumar_llista(l)"""

def sumar_lista(llista):
    suma = 0
    for valor in llista:
        suma += valor
    return suma 
ejemplo_lista = sumar_lista([2, 30, 4, 50])
print(f"Sumar: {ejemplo_lista}")

# Multiplicación lista
def multiplicar_lista(lista):
    producte = 1
    for valor in lista:
        producte *= valor 
    return producte 
ejemplo_lista = multiplicar_lista([2, 30, 4, 50])
print(f"Multiplicación: {ejemplo_lista}")