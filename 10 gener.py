"""def producte():

    a=int(input("Introdueix el primer nombre: "))
    b=int(input("Introdueix el segon nombre: "))

    print("El producte de {} i {} és {}".format(a, b, a * b))


a=producte()
"""

def producte():
    a=int(input("Introdueix el primer nombre: "))
    b=int(input("Introdueix el segon nombre: "))
    if b>a:
        print("La potencia de {} elevat a {} és {}".format(a, b, a ** b))
    else:
        print("La potencia de {} elevat a {} és {}".format(b, a, b ** a))


a=producte()