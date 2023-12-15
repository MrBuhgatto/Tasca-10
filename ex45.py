#Funció per llegir una llista fins que es posa un punt
def llegir_llista():
    a = []
    c = "a"
    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            a.append(c)
    return a

#Funció per eliminar els extrems d'una llista si té més de dos elements
def eliminar_capicua(a):
    b = []
    if len(a) > 2:
        b = a[1:-1]
    return b

#Programa principal
x = llegir_llista()
y = eliminar_capicua(x)
print("La llista original {} s'ha transformat en la llista {}".format(x, y))
