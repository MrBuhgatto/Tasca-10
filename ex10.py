#Definició de la funció 
def major(a):
    if a>18:
        print("És major d'edat") #Fa aquest print si el nombre introduit és major que 18
    elif a<18:
        print("És menor d'edat") #Fa aquest print si el nombre introduir és menor que 18
    else:
        print("Té 18 anys") #Fa aquest print si el nombre introduit és 18

#Programa principal
x = int(input("Introdueixi la seva edat: ")) #Et demana que introdueixis un nombre
major(x) #Crida a la funció 

