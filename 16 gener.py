a = input("Introdueix una paraula: ")
b = a[::-1]
for e in b:
    print("La paraula {} de l'enrevés és \n{}".format(a,e))