###Definir una funció crear_repetits() que agafi un número enter i un caràcter i retorni el caràcter multiplicat pel número enter. 
###Ex: crear_repetits(5, “a”), retorni “aaaaa”
def crear_repetits(a, b):
    c = b * int(a)
    return c

x = input("Introdueixi un número: ")
y = input("Introdueixi un caràcter: ")

# Convertir la entrada x a un número entero
try:
    x = int(x)
    print("El caràcter", y, "repetit", x, "-vegades és:", crear_repetits(x, y))
except ValueError:
    print("Si us plau, introdueix un número vàlid.")
