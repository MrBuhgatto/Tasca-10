def num_majuscules(s):
    nummajuscules = sum(c.isupper() for c in s)
    numminuscules = sum(c.islower() for c in s)
    numnumeros = sum(c.isdigit() for c in s)
    numcaractersespecials = len(s) - (nummajuscules + numminuscules + numnumeros)
    return nummajuscules, numminuscules, numnumeros, numcaractersespecials

# Programa principal
a = input("Indicar una paraula o una cadena de paraules: ")
nMaj, nMin, nNum, NCE = num_majuscules(a)

print(f"La paraula o cadena introduïda: {a} té:\n"
      f"{nMaj} Majúscules\n"
      f"{nMin} Minúscules\n"
      f"{nNum} Números\n"
      f"{NCE} Caràcters especials")
