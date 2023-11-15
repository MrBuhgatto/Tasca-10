def menu_principal():
    print("""
        Menú principal:
          1. Calculadora de enters
          2. Calculadora de reals
          3. Canvis de base
          4. Sortir   
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
# Def binari a
def bintooct(bin_num):
    dec_num = int(bin_num, 2)
    oct_num = oct(dec_num)
    return oct_num

def bintodec(bin_num):
    dec_num = int(bin_num, 2)
    return dec_num

def bintohex(bin_num):
    dec_num = int(bin_num, 2)
    hex_num = hex(dec_num)
    return hex_num[2:]

# Def octal a

def octtobin(oct_num):
    dec_num = int(oct_num, 8)
    bin_num = bin(dec_num)
    return bin_num[2:]

def octtodec(oct_num):
    dec_num = int(oct_num, 8)
    return dec_num

def octtohex(oct_num):
    dec_num = int(oct_num, 8)
    hex_num = hex(dec_num)
    return hex_num[2:]

# Def decimal to

def dectobin(dec_num):
    bin_num = bin(int(dec_num))
    return bin_num[2:]

def dectooct(dec_num):
    oct_num = oct(int(dec_num))
    return oct_num[2:]

def dectohex(dec_num):
    hex_num = hex(int(dec_num))
    return hex_num[2:]

# Def hexadecimal to

def hextobin(hex_num):
    dec_num = int(hex_num, 16)
    bin_num = bin(dec_num)
    return bin_num[2:]

def hextooct(hex_num):
    dec_num = int(hex_num, 16)
    oct_num = oct(dec_num)
    return oct_num[2:]

def hextodec(hex_num):
    dec_num = int(hex_num, 16)
    return dec_num

def canvi_base():
    print("Hem passat per canvi de base: ")
    op = 1
    while op>0:
        print("""
              Menú canvi de base
              1. Donat un binari ho passem a tota la resta
              2. Donat un octal ho passen a tota la resta
              3. Donat un decimal ho passem a tota la resta
              4. Donat un hexadecimal ho passem a tota la resta
              5. Sortir
        """)
        op = int(input("Elegeix una opció: "))
        match op:
            case 1: #Binari to 
                b = input("Introdueix el numero binari: ")
                c = bintooct(b)
                d = bintodec(b)
                e = bintohex(b)
                print("El nuemro binari {} es: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,c,d,e))

            case 2: #Octal to 
                b = input("Introdueix el numero octal: ")
                c = octtobin(b)
                d = octtodec(b)
                e = octtohex(b)
                print("El nuemro octal {} es: \n bin -> {} \n dec -> {} \n hex -> {}".format(b,c,d,e))
                
            case 3: #Decimal to 
                b = input("Introdueix el numero decimal: ")
                c = dectobin(b)
                d = dectooct(b)
                e = dectohex(b)
                print("El nuemro octal {} es: \n bin -> {} \n oct -> {} \n hex -> {}".format(b,c,d,e))
                
            case 4: #Hexadecimal to 
                b = input("Introdueix el numero hexadecimal: ")
                c = hextobin(b)
                d = hextooct(b)
                e = hextodec(b)
                print("El numero octal {} es: \n bin -> {} \n oct -> {} \n dec -> {}".format(b,c,d,e))

            case 5: #Sortir
                print("Adeu :,(")
                b = -1  
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
            canvi_base()
        case 4:
            a = -1
        case other:
            print("Opció no vàlida")