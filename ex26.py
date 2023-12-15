#Funció per filtrar paraules d'una llista segons una longitud mínima donada
def filtrar_paraules(a, num):
    b = list()
    for e in a:
        if num <= len(e):  #Comprova si la longitud de la paraula és igual o major a la longitud desitjada
            b.append(e)  #Afegeix la paraula filtrada a la nova llista
    return b

#Llista d'exemple
x = ["hola", "Sí", "Un senyor damunt un ruc", "filòsof", "Xouman", "Prototip"]
#Llegeix la longitud desitjada de les paraules
a = input("Indica la longitud de les paraules que vols filtrar: ")
#Filtra les paraules segons la longitud donada
y = filtrar_paraules(x, int(a))
#Imprimeix les paraules filtrades
print("Les paraules de igual o més longitud que", a, "són:", y)
