"""def conta_vocal():
    sum = 0
    a = ['a', 'e', 'i', 'o', 'u']
    b = input("Escriu una frase: ")
    b= b.lower()
    for e in b:
        if e in a:
            sum+=1
    print("La frase {} conté {} vocals".format(b, sum))

#PPrincipal
conta_vocal()"""

def conta_vocal():
    sum = 0
    sumc = 0
    sumca = 0
    a = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
    c = ['a','e','i','o','u']
    b = input("Escriu una frase: ")
    b= b.lower()
    for e in b:
        if e in c:
            sum+=1
        elif e in a:
            sumc+=1
        else:
            sumca+=1
    print("La frase {} conté {} vocals, {} consonants i {} caràcters especials".format(b, sum, sumc,sumca))

#PPrincipal
conta_vocal()

