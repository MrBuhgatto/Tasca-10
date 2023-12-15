#Funció que genera i mostra els nombres parells de 2 a 100
def parells():
    a = []
    for i in range(2, 101, 2):
        a.append(i)
    print("Els parells d'1 a 100 són {}".format(a))

#Funció que genera i mostra els nombres senars de 1 a 99
def senars():
    a = []
    for i in range(1, 100, 2):
        a.append(i)
    print("Els senars d'1 a 100 són {}".format(a))

#Programa principal
parells()
senars()
