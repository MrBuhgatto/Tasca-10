# Exercici 14: Definir una funció gran_de_tres(), donats tres números, retorni el major. Prova-la amb diferents exemples.

#Funció per trobar el número més gran entre tres nombres
def gran(a, b, c):
    if (a >= b):
        if (a >= c):
            return a
        else:
            return c
    else:
        if (b >= c):
            return b
        else:
            return c

#Entrada de tres nombres des de la terminal i crida a la funció gran
x = input("Introdueixi el primer número a comparar: ")
y = input("Introdueixi el segon número a comparar: ")
z = input("Introdueixi el tercer número a comparar: ")
c = gran(x, y, z)

#Mostra el resultat
print("El més gran és: ", c)




"""x = int(input("Introdueix el primer nombre: "))
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
print('El major de {} i {} és {}'. format(a,b,c))"""