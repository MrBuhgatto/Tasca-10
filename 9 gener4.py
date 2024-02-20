#Modificar funcio 3 perque enlloc de les inicials indiqui la longitud de cada paraula


def conta_inicial():
    a=input("Introdueix una frase: ")
    l=a.split(" ")
    c=[]
    d=['a','e','i','o','u']
    for e in l:
        if e[0] in d:
            c.append(e[0])
    print("Les paraules que comencen en vocal de la frase {} son {}".format(a,c))
#PPrincipal
conta_inicial()