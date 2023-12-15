#Inicialitza una llista buida
c = []

#Itera de 10 a 1 (decreixent)
for i in range(10, 0, -1):
    c.append(c)  # Afegeix la mateixa llista a cada iteració

print(c)  #Mostra la llista resultant, que contindrà 10 referències a la mateixa llista
