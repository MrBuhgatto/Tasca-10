#Inicialització de la suma i entrada d'un número
suma = 0
a = input("Introdueix un número: ")

#Mostra el nombre de dígits del número introduït
print("{} té {} dígits".format(a, len(a)))

#Itera pels dígits del número i mostra els dígits en posicions parelles
for i, e in enumerate(a):
    if i % 2 == 0:
        print("El dígit a la posició parella {} és {}".format(i, e))
