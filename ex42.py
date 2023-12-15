#Definició de la funció que mostra la taula de multiplicar d'un número donat fins a 20
def taula_multiplicar(a):
    for i in range(20):
        print("{} x {} = {}".format(i + 1, a, (i + 1) * a))

#Programa principal
x = int(input("Introdueixi un número per a calcular la seva taula de multiplicar: "))
taula_multiplicar(x)
