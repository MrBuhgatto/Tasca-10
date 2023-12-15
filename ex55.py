#Funció que dibuixa un patró d'estrelles
def dibuixar(a):
    l = []
    #Dibuixa mitja piràmide ascendent
    for j in range(a + 1):
        for i in range(j):
            l.append('*')
        print(' '.join(map(str, l)))
        l.clear()
    
    #Dibuixa mitja piràmide descendent
    for j in range(a + 1, 0, -1):
        for i in range(j):
            l.append('*')
        print(' '.join(map(str, l)))
        l.clear()

#Programa principal
a = int(input("Introdueixi un número: "))
dibuixar(a)
