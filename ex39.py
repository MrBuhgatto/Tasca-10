x = int(input("Introdueixi un número natural (<100): "))
suma = 0

#Itera en decreixent de 4 en 4 fins a 0, suma els quadrats i ho mostra
for i in range(x, 0, -4):
    suma = suma + (i**2)

print("La suma dels quadrats de 4 posicions menys de {} és {} ".format(x, suma))
