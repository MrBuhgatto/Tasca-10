### Definir una funció superposicio() que agafi dues llistes i retorni vertader si hi ha un element en comú, en cas contrari, que retorni fals.

def superposicio():
    a=list(input('Introdueix una llista: '))
    b=list(input('Introdueix una llista: '))
    for c in a:
        if c in b:
            print('True')
        else:
            print('False')    
a=superposicio()