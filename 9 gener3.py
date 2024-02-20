def conta_inicial():
    a=input("Introdueix una frase: ")
    l=a.split(" ")
    c=[]
    for e in l:
        c.append(e[0])
    print("La primera palabra de la frase {} es {}".format(a,c))
#PPrincipal
conta_inicial()