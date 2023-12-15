#Inicialització de la suma i entrada d'un número
suma = 0
a = input("Introdueix un número: ")

#Mostra el nombre de dígits del número introduït
print("{} té {} dígits".format(a, len(a)))

#Suma dels dígits del número
for i in a:
    suma = suma + int(i)

#Mostra la suma i indica si és parell o senar
print("La suma dels dígits del número {} és {}".format(a, suma))
if suma % 2 == 0:
    print("La suma dels dígits del número {} és parell".format(a))
else:
    print("La suma dels dígits del número {} és senar".format(a))
