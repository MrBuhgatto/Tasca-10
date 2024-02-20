def divisió():
    a=int(input("Introdueix el primer nombre: "))
    b=int(input("Introdueix el segon nombre: "))
    if b>0 and b<6 or b>9 and b<21:
        print("La divisió de {} i {} és {}".format(a, b, a / b))
    else:
        print("Error")


a=divisió()