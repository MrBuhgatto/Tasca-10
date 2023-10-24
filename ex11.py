def menu_principal():
    print("""
        Menú principal:
          1. Calculadora de enters
          2. Calculadora de reals
          3. Sortir
          """)
    x = int(input("Elegeix una opció: "))
    if x>0 and x<4:
        return x
    else:
        return 0
        
#Programa principal
a = menu_principal
print(a)