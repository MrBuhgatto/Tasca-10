"""
def contar_as():
    b=('a')
    a=[0]
    for i, e in enumerate(c):
        if e in ('a'):
            a[0] += 1
        else:
            a[0] += 1
    for i, e in enumerate(c):
        print("La lletra {} apareix {} vegades".format(b[i], a[i]))        

#PPrincipal
c = input("Introdueixi una paraula a analitzar: ")
contar_as(c)
"""
def contar_as(a,u,l):
    num=0
    onum=0
    for e in a:
        if e == u:
            num= num + 1
        if a == l:
            onum = onum + 1
    print("La frase {} té {} d'{} i té {} d'{}".format(a,num,u,onum,l))

#PPrincipal
a = input("Introdueixi una paraula a analitzar: ")
l = input("Introdueix caracter: ")
u = input("Introdueix un altre caracter: ")
contar_as(a,u,l)