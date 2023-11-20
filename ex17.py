###Definir una funció sumar_llista() i una funció multiplicar_llista() que sumin i multipliqueu, respectivament, tots els valors d’una llista. 
###Prova-la amb diferents exemples. Ex: sumar_llista([1,2,3,4]) retorni 10.

def menu_principal():
    print("""
        Menú principal:
          1. Sumar llista
          2. Multiplicar llista
          3. Sortir 
    """)
    a = int(input("Elegeix una opció: "))

def sumar_llista():
    x=1
    
    a=input('Introdueix una llista: ')

    c=list(a)

    sum(a)
    while x!=1:
        match a:
            case 1:
                print('La suma de la llista {} és igual a {}'.format (a,c))
            case other:
                print('Torna a provar')
def sumar_llista():
    x=1
    a=input('Introdueix una llista: ')
    c=list(a)

    while x!=1:
        match a:
            case 1:
                print('La multiplicació de la llista {} és igual a {}'.format (a,c))
            case other:
                print('Torna a provar')

#Programa principal
a = 1
while a>0:
    a=menu_principal()
    match a:
        case 1:
            sumar_llista()
        case 2:
            multiplicar_llista()
        case 3:
            a = -1
        case other:
            print("Opció no vàlida")

