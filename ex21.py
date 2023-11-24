###Definir una funció crear_repetits() que agafi un número enter i un caràcter i retorni el caràcter multiplicat pel número enter. 
###Ex: crear_repetits(5, “a”), retorni “aaaaa”

def crear_repetits():
    a=input('Introdueix un caràcter: ')
    b=int(input('Introdueix un número: '))
    print(a * int(b))
    
a=crear_repetits()