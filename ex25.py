###Definir una funció paraula_mes_llarga() que donada una llista de paraules, retorni la que té més caràcters. 
###Ex: paraula_mes_llarga([“Hola”, “Ramis”, “IES”, “Paraula”]), ens retorni Paraula.
#Funció per llegir una llista d'elements fins que es introdueix el caràcter '.'
def llegir_llista():
    a = 'o'
    l = []
    while a != '.':
        a = input("Introdueix una llista: ")
        if a == '.':
            l.append(int(a))  #Afegeix l'element a la llista si és diferent de '.'
        else:
            return l

#Funció que troba la paraula més llarga en una llista de paraules
def paraula_mes_llarga(a):
    max = a[0]
    for n in a:
        if len(n) > len(max):  #Compara la longitud de cada paraula amb la longitud màxima trobada fins ara
            max = n
    return max

#Programa principal
l = llegir_llista()  #Llegeix la llista d'elements
print("La paraula més llarga de la llista {} és {}".format(l, paraula_mes_llarga(l)))
