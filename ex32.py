#Funció que compta i mostra els noms que comencen amb una lletra específica en una llista
def noms_que_comencen_per(llista, lletra):
    comptador = 0  #Inicialitza el comptador de noms
    llnom = []  #Inicialitza la llista de noms que comencen amb la lletra
    for e in llista:
        if e[0] == lletra:  #Verifica si el primer caràcter del nom és la lletra buscada
            llnom.append(e)  #Afegeix el nom a la llista
            comptador += 1 
    print("El número de noms que comencen per el caràcter {} són: {} i són: {}".format(lletra, comptador, llnom))

#Funció per llegir noms fins que es posi -1 i retornar la llista
def llegir_noms():
    i = 0
    l = []
    print("Introdueixi noms a la llista, per acabar posau -1: ")
    while i > -1:
        l.append(input("Posi el següent nom: "))  #Afegeix el nom a la llista
        if l[i] == "-1":
            l.remove("-1")
            i = -5  #Si es posa -1, surt del bucle
        i += 1  #Incrementa l'índex
    return l  #Retorna la llista de noms

#Programa principal
noms = llegir_noms()  #Crida a la funció per llegir noms
noms_que_comencen_per(noms, "a")  #Crida a la funció per mostrar noms que comencen amb la lletra especificada

 