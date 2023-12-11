###Definir una funció invertir() que calculi la inversa d’una cadena. Ex: invertir(“Soc del Ramis”) hauria de tornar la cadena “simaR led coS”.

def invertir(a):
	b = list(a)
	c = b[::-1]
	r = "".join(c)
	return r
# Programa principal
s="Això és una cadena que sha de girar"
print("La cadena: “, x, “ girada és: ",invertir(s))
		