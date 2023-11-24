###Definir una funció que agafi un caràcter i retorni vertader si és una vocal i en cas contrari retorni fals. 
###Prova-la amb diferents exemples.

def llegir_caràcter():
    a= 'b'
    while a!='-a':
        a=input('Introdueix un caràcter: ')
        if a == ('a'):
            print('vertader')
        elif a == ('e'):
            print('vertader')
        elif a == ('i'):
            print('vertader')
        elif a == ('o'):
            print('vertader')
        elif a == ('u'):
            print('vertader')
        else:
            print('fals') 
                
# Programa principal
a= llegir_caràcter()