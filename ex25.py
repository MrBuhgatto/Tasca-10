###Definir una funció paraula_mes_llarga() que donada una llista de paraules, retorni la que té més caràcters. 
###Ex: paraula_mes_llarga([“Hola”, “Ramis”, “IES”, “Paraula”]), ens retorni Paraula.
def llegir_llista():
    a= 'o'
    l=[]
    while a!='.':
        a=input("Introdueix una llista: ")
        if a == '.':
            l.append(int(a))
        else:
            return l

def paraula_mes_llarga(a):
    max = a[0]
    for n in a:
        if len(n) > len(max):
            max = n
    return max

#Programa principal
l = llegir_llista()
print("La paraula més llarga de la llista {} és {}".format(l,paraula_mes_llarga(l)))