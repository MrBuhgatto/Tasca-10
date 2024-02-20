a = input("Introdueix una paraula: ")
b = ("a","á","à","e","è","é","i","ì","í","o","ò","ó","u","ù","ú")
c = ("b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z")
h = []
z = []
y = []
for e in a:
    lower = e.lower()
    if lower in b:
        z.append(e)
    elif lower in c:
        h.append(e)
    else:
        y.append(e)
print("Les vocals de la paraula {} son {}, les consonants {} i els caràcters especials {}".format(a,h,z,y))
