###Definir una funció invertir() que calculi la inversa d’una cadena. Ex: invertir(“Soc del Ramis”) hauria de tornar la cadena “simaR led coS”.

def invertir():
    a=("Soc del ramis")
    print("El valor abans d'invertir-lo és: \n {}".format(a))
    b=a [::-1]
    print("El valor després d'invertir-lo és: \n {}".format(b))
    
a=invertir()