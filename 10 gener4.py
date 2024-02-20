"""
a=(int(input("Introdueix el primer nombre: ")))
b=(int(input("Introdueix el segon nombre: ")))
if a>5 and b<5:
    print("La divisió de {} i {} és {}".format(a,b,a/b))
elif a<5 and b<10:
    print("La divisió de {} i {} és {}".format(b,a,b/a))
else:
    print("Error")
"""
a=input("Introdueix la primera paraula: ")
b= len(a)
match b:
    case 1:
        print("La longitud de la paraula {} és un".format(a))
    case 2:
        print("La longitud de la paraula {} és dos".format(a))
    case 3:
        print("La longitud de la paraula {} és tres".format(a))
    case 4:
        print("La longitud de la paraula {} és quatre".format(a))
    case 5:
        print("La longitud de la paraula {} és cinc".format(a))
    case other:
        print("La longitud de la paraula {} és superior a cinc".format(a))  
