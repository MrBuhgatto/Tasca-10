#Funció per comptar el nombre de majúscules, minúscules, números i caràcters especials en una cadena
def num_majuscules(s):
    nummajuscules = sum(c.isupper() for c in s)
    numminuscules = sum(c.islower() for c in s)
    numnumeros = sum(c.isdigit() for c in s)
    numcaractersespecials = len(s) - (nummajuscules + numminuscules + numnumeros)
    return nummajuscules, numminuscules, numnumeros, numcaractersespecials

#Programa principal
a = input("Indica una paraula o una cadena de paraules: ")
#Obté les dades sobre majúscules, minúscules, números i caràcters especials
nMaj, nMin, nNum, NCE = num_majuscules(a)
#Imprimeix els resultats
print(f"La paraula o cadena introduïda: {a} té:\n"
      f"{nMaj} Majúscules\n"
      f"{nMin} Minúscules\n"
      f"{nNum} Números\n"
      f"{NCE} Caràcters especials")
