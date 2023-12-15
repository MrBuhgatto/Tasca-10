#Funció per convertir un nombre binari a decimal
def bintodec(bin):
    return int(bin, 2)

#Funció per convertir una llista de nombres binaris a nombres decimals
def llbintodec(llbin):
    lldec = [bintodec(e) for e in llbin]
    return lldec

#Programa principal
#Llista de nombres binaris
a = ["111", "11", "1010", "1000"]
# Converteix la llista de nombres binaris a decimals
b = llbintodec(a)

#Imprimeix els resultats
for binario, decimal in zip(a, b):
    print(f"El número binari: {binario} correspon amb el número decimal: {decimal}")
