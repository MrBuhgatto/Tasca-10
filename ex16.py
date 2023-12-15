###Definir una funció que agafi un caràcter i retorni vertader si és una vocal i en cas contrari retorni fals. 
###Prova-la amb diferents exemples.

#Funció per llegir un caràcter i verificar si és una vocal
def llegir_caràcter():
    a = 'b'
    while a != '-a':
        a = input('Introdueix un caràcter: ')
        if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
            print('Vertader')
        else:
            print('Fals') 

#Programa principal
llegir_caràcter() #Crida a la funció
