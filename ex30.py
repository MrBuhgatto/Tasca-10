def mostrar_majors_que(t, nreferencia):
    #Imprimeix tots els números majors que la referència
    print("Tots els números majors de {} són: ".format(nreferencia))
    for e in t:
        if e > nreferencia:
            print("{} ".format(e))

def llegir_tupla():
    #Inicialitza una llista buida per a la tupla
    a = []
    print("Introdueixi tots els números que vulguis. Per aturar posi -1: ")
    while True:
        #Demana a l'usuari introduir un número
        num = input("Introdueixi un número: ")
        if num == "-1":
            #Si es posa -1, surt del bucle
            break
        #Converteix el número a enter i l'afegeix a la llista
        a.append(int(num))
    #Retorna una tupla amb els números introduïts
    return tuple(a)

#Programa principal
#Demana a l'usuari introduir un número de referència
referencia = int(input("Introdueixi el número que voleu comparar: "))
#Obté la tupla de números mitjançant la funció llegir_tupla
tupla_numeros = llegir_tupla()
#Crida la funció mostrar_majors_que per imprimir els números majors que la referència
mostrar_majors_que(tupla_numeros, referencia)

