def menu_principal():
    print("""
        Menú principal:
          1. Calculadora de enters
          2. Calculadora de reals
          3. Calculadora de binari
          4. Clculadora de octal
          5. Calculadora de hexadecimal
          6. Sortir
    
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
       
def calculadora_binari():
    print("Has triat la calculadora d'enters")
    d = 1
    while d>0:
        print(""" 
              1. Binari a decimal 
              2. Decimal a binari
              3. Sortir
        """)
        d = int(input("Elegeix una opció: "))
        match d:
            case 1: #Binari a decimal
                def binario_decimal():
	                numero = int(input('Introduce un número:\n'))
	            convertido = bin(numero)
	            print(convertido)
                    binario_decimal()

            case 2: #Decimal a binari
                x = bin(input("Introdueix el primer nombre: "))
                y = bin(input("Elegeix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))

            case 3: #Sortir
                print("Adeu :,(")
                d = -1

def calculadora_octal():
    print("Has triat la calculadora d'enters")
    e = 1
    while e>0:
        print(""" 
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Salir
        """)
        e = int(input("Elegeix una opció: "))
        match e:
            case 1: #Sumar
                x = oct(input("Introdueix el primer nombre: "))
                y = oct(input("Elegeix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))

            case 2: #Restar
                x = int(oct,("Introdueix el primer nombre: "))
                y = int(oct, 8("Elegeix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            
            case 3: #Multiplicar
                x = oct(input("Introdueix el primer nombre: "))
                y = oct(input("Elegeix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            
            case 4: #Dividir
                x = oct(input("Introdueix el primer nombre: "))
                y = oct(input("Elegeix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))

            case 5: #Sortir
                print("Adeu :,(")
                e = -1
            
def calculadora_hexadec():
    print("Has triat la calculadora d'enters")
    f = 1
    while f>0:
        print(""" 
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Salir
        """)
        f = int(input("Elegeix una opció: "))
        match f:
            case 1: #Sumar
                x = hex(input("Introdueix el primer nombre: "))
                y = hex(input("Elegeix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))

            case 2: #Restar
                x = hex(input("Introdueix el primer nombre: "))
                y = hex(input("Elegeix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            
            case 3: #Multiplicar
                x = hex(input("Introdueix el primer nombre: "))
                y = hex(input("Elegeix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            
            case 4: #Dividir
                x = hex(input("Introdueix el primer nombre: "))
                y = hex(input("Elegeix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))

            case 5: #Sortir
                print("Adeu :,(")
                f = -1
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
            calculadora_binari()
        case 4:
            calculadora_octal()
        case 5:
            calculadora_hexadec()
        case 6:
            a = -1
        case other:
            print("Opció no vàlida")