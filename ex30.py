def mostrar_majors_que(t, nreferencia):
    print("Tots els números majors de {} són: ".format(nreferencia))
    for e in t:
        if e > nreferencia:
            print("{} ".format(e))

def llegir_tupla():
    a = []
    print("Introdueixi tots els números que vulguis. Per aturar posi -1: ")
    while True:
        num = input("Introdueixi un número: ")
        if num == "-1":
            break
        a.append(int(num))
    return tuple(a)

# Programa principal
referencia = int(input("Introdueixi el número que voleu comparar: "))
tupla_numeros = llegir_tupla()
mostrar_majors_que(tupla_numeros, referencia)
