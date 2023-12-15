# Exercici 13: Definir una funció gran() que, donats dos números, retorni el major.  Prova-la amb diferents exemples.
#Funció per obtenir el número major entre dos nombres
def major(n, m):
    if n > m:
        return n
    else:
        return m

#Entrada de dos nombres
a = int(input('Introdueix el primer número: '))
b = int(input('Introdueix el segon número: '))

#Crida a la funció major i mostra el resultat
c = major(a, b)
print('El major entre {} i {} és {}'.format(a, b, c))

