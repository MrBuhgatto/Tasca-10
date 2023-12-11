###Definir una funció gran_llista() que donada una llista de número ens retorni el més gran. 
###Ex: gran_llista([3, 4, 2, 3, 10]), retorni 10.

def gran_llista(a):
    a.sort()
    return a[-1]

# Programa principal
a = [3, 40, 34, 15, 4, 5, 7, 9]
c = gran_llista(a)
print(c)
