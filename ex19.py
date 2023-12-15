### Definir una funció es_palindrom() que retorni vertader si li passem un palíndrom i fals en cas contrari.
### Un palíndrom és una paraula que s’escriu igual d’esquerra a dreta i de dreta a esquerra. 
### Per exemple: radar, ara, civic, rallar, tapat, simis, refer, ...
#Funció per comprovar si una paraula és un palíndrom
def es_palindrom():
    a = input("Introdueix una paraula: ")
    y = a[::-1]
    x = a
    b = y
    if a == b:
        print("{} és un palíndrom".format(a))
    else:
        print("{} no és un palíndrom".format(a))

#Programa principal
a = es_palindrom() #Crida a la funció

