###Definir una funció gran_llista() que donada una llista de número ens retorni el més gran. 
###Ex: gran_llista([3, 4, 2, 3, 10]), retorni 10.

def gran_llista():
    a= list(input('Introdueix una llista: '))
    a.sort()
    c=a[-1]
    print(c)
a=gran_llista()

#Funciona amb nombres de 0 a 9