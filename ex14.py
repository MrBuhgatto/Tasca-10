# Exercici 14: Definir una funció gran_de_tres(), donats tres números, retorni el major. Prova-la amb diferents exemples.



x = int(input("Introdueix el primer nombre: "))
y = int(input("Introdueix el segon nombre: "))
z = int(input("Introdueix el tercer nombre: "))

if x>y>z:
    print("El nombre més gran és: {}".format(x))

elif x>z>y:
    print("El nombre més gran és: {}".format(x))

elif x>y==z:
    print("El nombre més gran és: {}".format(y))

elif z>x>y:
    print("El nombre més gran és: {}".format(z))

elif y>x>z:
    print("El nombre més gran és: {}".format(y))

elif y>z>x:
    print("El nombre més gran és: {}".format(y))

elif y>x==z:
    print("El nombre més gran és: {}".format(y))

elif z>y>x:
    print("El nombre més gran és: {}".format(z))

elif y==z>x:
    print("El nombre més gran és: {}".format(y))

elif x==y>z:
    print("El nombre més gran és: {}".format(y))

elif x==y==z:
    print("Tots tres nombres son iguals")

else:
    print("Tots tres nombres son iguals")

def major(n,m,ñ):
    if n>m>ñ:
        return n
    else:
        return m
a= int(input('Intro el 1r numero: '))
b= int(input('Intro el 2r numero: '))
c= major(a,b)
print('El major de {} i {} és {}'. format(a,b,c))