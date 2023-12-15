#Funció que compta i mostra els noms que comencen amb una lletra específica en una llista
def noms_que_comencen_per(llista, lletra):
    comptador = 0
    llnom = []
    for e in llista:
        if e[0] == lletra:
            llnom.append(e)
            comptador += 1
    print("Noms que comencen amb la lletra {}: {} i són: {}".format(lletra, comptador, llnom))

#Funció per llegir noms fins que es posi -1 i retornar la llista
def llegir_noms():
    i = 0
    l = []
    print("Introdueixi noms a la llista, per acabar posau -1: ")
    while i > -1:
        l.append(input("Posi el següent nom: "))
        if l[i] == "-1":
            l.remove("-1")
            i = -5
        i += 1
    return l

#Programa principal
noms = llegir_noms()  #Crida a la funció per llegir noms
lletra = "a" 
noms_que_comencen_per(noms, lletra)  #Trucada a la funció per mostrar noms que comencen amb la lletra especificada

