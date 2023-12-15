def menu_principal():
    #Mostra el menú principal
    print("""
        Menú principal:
          1. Calculadora d'enters
          2. Calculadora de reals
          3. Canvis de base
          4. Sortir   
    """)
    a = int(input("Elegeix una opció: "))  # Llegeix l'opció seleccionada per l'usuari
    return a  #Retorna l'opció escollida

def calculadora_enters():
    print("Has triat la calculadora d'enters")
    b = 1
    #Inicia el bucle
    while b > 0: 
        print(""" 
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Sortir
        """)  #Mostra les operacions disponibles
        b = int(input("Elegeix una opció: "))
        match b:
            case 1:  #Suma
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Elegeix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))

            case 2:  #Resta
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Elegeix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            
            case 3:  #Multiplicació
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Elegeix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))

            case 4:  #Divisió
                x = int(input("Introdueix el primer nombre: "))
                y = int(input("Elegeix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))

            case 5:  #Sortir
                print("Adeu :,(")
                b = -1  #Finalitza el bucle

def calculadora_reals():
    print("Has triat la calculadora de reals: ")
    c = 1
    #Inici del bucle
    while c > 0:
        print(""" 
              1. Sumar 
              2. Restar
              3. Multiplicar 
              4. Dividir
              5. Sortir
        """)  #Mostra les operacions disponibles
        c = int(input("Elegeix una opció: "))
        match c:
            case 1:  #Suma
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print("{} + {} = {}".format(x, y, x+y))

            case 2:  #Resta
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print("{} - {} = {}".format(x, y, x-y))
            
            case 3:  #Multiplicació
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print("{} * {} = {}".format(x, y, x*y))
            
            case 4:  #Divisió
                x = float(input("Introdueix el primer nombre: "))
                y = float(input("Elegeix el segon nombre: "))
                print("{} / {} = {}".format(x, y, x/y))
            
            case 5:  #Sortir
                print("Adeu :,(")
                c = -1  #Finalitza el bucle

#Funcions de conversió binària
def bintooct(bin_num):
    #Converteix binari a octal
    dec_num = int(bin_num, 2)
    oct_num = oct(dec_num)
    return oct_num

def bintodec(bin_num):
    #Converteix binari a decimal
    dec_num = int(bin_num, 2)
    return dec_num

def bintohex(bin_num):
    #Converteix binari a hexadecimal
    dec_num = int(bin_num, 2)
    hex_num = hex(dec_num)
    return hex_num[2:]

#Funcions de conversió octal
def octtobin(oct_num):
    #Converteix octal a binari
    dec_num = int(oct_num, 8)
    bin_num = bin(dec_num)
    return bin_num[2:]

def octtodec(oct_num):
    #Converteix octal a decimal
    dec_num = int(oct_num, 8)
    return dec_num

def octtohex(oct_num):
    #Converteix octal a hexadecimal
    dec_num = int(oct_num, 8)
    hex_num = hex(dec_num)
    return hex_num[2:]

# Funcions de conversió decimal
def dectobin(dec_num):
    #Converteix decimal a binari
    bin_num = bin(int(dec_num))
    return bin_num[2:]

def dectooct(dec_num):
    #Converteix decimal a octal
    oct_num = oct(int(dec_num))
    return oct_num[2:]

def dectohex(dec_num):
    #Converteix decimal a hexadecimal
    hex_num = hex(int(dec_num))
    return hex_num[2:]


#Funcions per la conversió hexadecimal
def hextonum(hex):
    #Converteix un dígit hexadecimal a decimal
    pnum = {"f": 15, "e": 14, "d": 13, "c": 12, "b": 11, "a": 10}
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)

def hextodec2(hex):
    #Converteix nombre hexadecimal a decimal
    hex = hex.lower()
    hex = hex[::-1]
    decimal = 0
    posicio = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * valor
        decimal += pnum
        posicio += 1
    return decimal

def hextobin(numero):
    #Converteix nombre hexadecimal a binari
    a = int(numero, 16)
    return dectobin(a)

def hextooct(numero):
    #Converteix nombre hexadecimal a octal
    a = int(numero, 16)
    return dectooct(a)

def hextodec(numero):
    #Converteix nombre hexadecimal a decimal
    a = int(hextodec2(numero))
    return a

#Funció per al canvi de base
def canvi_base():
    print("Hem passat per canvi de base: ")
    op = 1
    while op > 0:
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
            case 1:  #Binari to 
                b = input("Introdueix el número binari: ")
                c = bintooct(b)
                d = bintodec(b)
                e = bintohex(b)
                print("El número binari {} és: \n oct -> {} \n dec -> {} \n hex -> {}".format(b, c, d, e))

            case 2:  #Octal to 
                b = input("Introdueix el número octal: ")
                c = octtobin(b)
                d = octtodec(b)
                e = octtohex(b)
                print("El número octal {} és: \n bin -> {} \n dec -> {} \n hex -> {}".format(b, c, d, e))
                
            case 3:  #Decimal to 
                b = input("Introdueix el número decimal: ")
                c = dectobin(b)
                d = dectooct(b)
                e = dectohex(b)
                print("El número octal {} és: \n bin -> {} \n oct -> {} \n hex -> {}".format(b, c, d, e))
                
            case 4:  #Hexadecimal to 
                b = input("Introdueix el número hexadecimal: ")
                c = hextobin(b)
                d = hextooct(b)
                e = hextodec(b)
                print("El número octal {} és: \n bin -> {} \n oct -> {} \n dec -> {}".format(b, c, d, e))

            case 5:  #Sortir
                print("Adeu :,(")
                b = -1  

#Programa principal
a = 1  #Inicia variable del menú
while a > 0: #Bucle principal
    a = menu_principal() #Rep la opció del menú
    match a:
        case 1: #Inicia la calculadora d'enters
            calculadora_enters() #Crida a la funció
        case 2: #Calculadora de reals
            calculadora_reals() #Crida a la funció
        case 3: #Canvi de base
            canvi_base() #Crida a la funció
        case 4: #Sortir
            a = -1 #Finalitza el bucle principal
        case other:
            print("Opció no vàlida")
