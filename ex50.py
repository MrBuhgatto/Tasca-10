#Funció per llegir un fitxer i crear una llista amb les seves línies
def crear_llista_fitxer(fitxer):
    with open(fitxer, 'r') as f:
        llista = f.readlines()
    lparaules = [linea.rstrip('\n') for linea in llista] 
    print(lparaules)

#Programa principal: crida la funció amb la ruta del fitxer com a argument
crear_llista_fitxer('/home/cicles/AO/Tasca-10/prova.txt')
