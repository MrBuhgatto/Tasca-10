def bintodec(bin):
    return int(bin, 2)

def llbintodec(llbin):
    lldec = [bintodec(e) for e in llbin]
    return lldec

# Programa principal
a = ["111", "11", "1010", "1000"]
b = llbintodec(a)

for binario, decimal in zip(a, b):
    print(f"El número binari: {binario} correspon amb el número decimal: {decimal}")
