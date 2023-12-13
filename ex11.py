# Definició de la funció pel menú principal
def menu_principal():
    print("""
        Menú principal:
          1. Calculadora d'enters
          2. Calculadora de reals
          3. Sortir
    """)  # Menú amb opcions de calculadores
    a = int(input("Tria una opció: "))  # Selecciona la calculadora
    return a  # Retorna l'opció triada


# Funció per a la calculadora d'enters
def calculadora_enters():
    print("Has triat la calculadora d'enters")
    b = 1  # Inicialitza el bucle
    while b > 0:  # Bucle d'operacions
        print("""
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Sortir
        """)  # Operacions disponibles
        b = int(input("Tria una opció: "))  # Selecciona una operació
        match b:
            case 1:  # Sumar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Tria el segon nombre: "))
                print("{} + {} = {}".format(x, y, x + y))

            case 2:  # Restar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Tria el segon nombre: "))
                print("{} - {} = {}".format(x, y, x - y))

            case 3:  # Multiplicar
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Tria el segon nombre: "))
                print("{} * {} = {}".format(x, y, x * y))

            case 4:  # Dividir
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Tria el segon nombre: "))
                print("{} / {} = {}".format(x, y, x / y))

            case 5:  # Sortir
                print("Adéu :,(")
                b = -1  # Finalitza el bucle



# Función para el menú principal
def menu_principal():
    print("""
        Menú principal:
          1. Calculadora de enteros
          2. Calculadora de reales
          3. Salir
    """)  # Menú de opciones
    a = int(input("Elige una opción: "))  # Selección de opción
    return a  # Retorna la opción elegida


# Función para la calculadora de enteros
def calculadora_enters():
    print("Has elegido la calculadora de enteros")
    b = 1  # Inicializa el bucle
    while b > 0:  # Comienza el bucle
        print("""
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Salir
        """)  # Operaciones disponibles
        b = int(input("Elige una opción: "))  # Selección de operación
        match b:
            case 1:  # Sumar
                x = int(input("Ingresa el primer número: "))
                y = int(input("Elige el segundo número: "))
                print("{} + {} = {}".format(x, y, x + y))

            case 2:  # Restar
                x = int(input("Ingresa el primer número: "))
                y = int(input("Elige el segundo número: "))
                print("{} - {} = {}".format(x, y, x - y))

            case 3:  # Multiplicar
                x = int(input("Ingresa el primer número: "))
                y = int(input("Elige el segundo número: "))
                print("{} * {} = {}".format(x, y, x * y))

            case 4:  # Dividir
                x = int(input("Ingresa el primer número: "))
                y = int(input("Elige el segundo número: "))
                print("{} / {} = {}".format(x, y, x / y))

            case 5:  # Salir
                print("Adiós :,(")
                b = -1  # Finaliza el bucle


# Función para la calculadora de reales
def calculadora_reals():
    print("Has elegido la calculadora de reales: ")
    c = 1
    while c > 0:
        print("""
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Salir
        """)  # Operaciones disponibles
        c = int(input("Elige una opción: "))
        match c:
            case 1:  # Sumar
                x = float(input("Ingresa el primer número: "))
                y = float(input("Elige el segundo número: "))
                print("{} + {} = {}".format(x, y, x + y))

            case 2:  # Restar
                x = float(input("Ingresa el primer número: "))
                y = float(input("Elige el segundo número: "))
                print("{} - {} = {}".format(x, y, x - y))

            case 3:  # Multiplicar
                x = float(input("Ingresa el primer número: "))
                y = float(input("Elige el segundo número: "))
                print("{} * {} = {}".format(x, y, x * y))

            case 4:  # Dividir
                x = float(input("Ingresa el primer número: "))
                y = float(input("Elige el segundo número: "))
                print("{} / {} = {}".format(x, y, x / y))

            case 5:  # Salir
                print("Adiós :,(")
                c = -1  # Finaliza el bucle


# Programa principal
a = 1  # Inicia la variable del menú
while a > 0:  # Bucle principal
    a = menu_principal()  # Rep la opció del menú
    match a:
        case 1:  # Inicia la calculadora d'enters
            calculadora_enters()  # Crida a la funció
        case 2:  # Calculadora de reals
            calculadora_reals()  # Crida a la funció
        case 3:  # Sortir
            a = -1  # Finalitza el bucle principal
        case other:  # Opció no vàlida
            print("Opció no vàlida")

