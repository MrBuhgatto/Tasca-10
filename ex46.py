#Funció per verificar si una llista està ordenada ascendentment, descendentment o no està ordenada
def esta_ordenada(a):
    b = a.copy()
    c = a.copy()
    b.sort()
    c.sort(reverse=True)
    if a == b:
        print("La llista {} està ordenada ascendentment {}".format(a, b))
    elif a == c:
        print("La llista {} està ordenada descendentment {}".format(a, c))
    else:
        print("La llista {} no està ordenada {}".format(a, b))

#Funció per llegir una llista fins que es posa un punt
def llegir_llista():
    a = []
    c = "a"
    while c != ".":
        c = input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c != ".":
            a.append(c)
    return a

#Programa principal
a = llegir_llista()
esta_ordenada(a)
