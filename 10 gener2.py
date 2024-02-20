def divisió():
    a=int(input("Introdueix el primer nombre: "))
    b=int(input("Introdueix el segon nombre: "))
    if b>0:
        print("La divisió de {} i {} és {}".format(a, b, a / b))
    else:
        print("Error, no es pot dividir un nombre per 0")


a=divisió()