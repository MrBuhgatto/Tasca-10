### Ex. 15: Definir una funció que calculi la longitud d’una llista o d’una cadena donada. 
### Prova-la amb diferents exemples.

#Funció per calcular la longitud d'una llista o cadena de caràcters
def longitud_llista(b):
    return len(str(b))

#Entrada de l'usuari i crida a la funció per calcular la longitud
a = input('Introdueix una llista o cadena de caràcters: ')
c = longitud_llista(a)

#Mostra el resultat
print('La llista o cadena {} té {} caràcters'.format(a, c))
