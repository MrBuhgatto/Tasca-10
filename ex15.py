### Ex. 15: Definir una funció que calculi la longitud d’una llista o d’una cadena donada. 
### Prova-la amb diferents exemples.

def longitud_llista(b):
        return len(str(b))

a= input('Introdueix una llista o cadena de caràcters: ')
c= longitud_llista(a)
print('La llista o cadena {} té {} caràcters'.format(a,c))
