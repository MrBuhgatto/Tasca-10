def menu_principal():
    print("""
        Menú principal:
          1. Calculadora de enters
          2. Calculadora de reals
          3. Sortir
    
    """)
    a = int(input("Elegeix una opció: "))
    return a
def calculadora_enters():
    print("Has triat la calculadora d'enters")
    b = 1
    while b>0:
        print(""" 
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Salir
        """)
        b = int(input("Elegeix una opció: "))
        match b:
            case 1: #Sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Elegeix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))

            case 2: #Restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Elegeix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            
            case 3: #Multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Elegeix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            
            case 4: #Dividir
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Elegeix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))

            case 5: #Sortir
                print("Adeu :,(")
                b = -1
       


def calculadora_reals():
    print("Has triat la calculadora de reals: ")
    c = 1
    while c>0:
        print(""" 
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Salir
        """)
        c = int(input("Elegeix una opció: "))
        match c:
            case 1: #Sumar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))

            case 2: #Restar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            
            case 3: #Multiplicar
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            
            case 4: #Dividir
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            
            case 5: #Sortir
                print("Adeu :,(")
                c = -1
       
        
#Programa principal

a = 1
while a>0:
    a=menu_principal()
    match a:
        case 1:
            calculadora_enters()
        case 2:
            calculadora_reals()
        case 3:
            a = -1
        case other:
            print("Opció no vàlida")