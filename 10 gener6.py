"""def llegir_llista():
    a = '1'
    b = []
    while a != 'fi':
        a= input("Introdueix una llista entera i posa 'fi' per aturar: ")
        if a != 'fi':
            b.append(int(a))
        else:
            return b

def filtrar_edats(l):
    a= []
    b= []
    for e in l:
        if e >=18:
            a.append(e)
        else:
            b.append(e)
    print("Els majors d'edat son {} i els menors d'edat son {}".format(a,b))

#PPrincipal 
a = llegir_llista()
filtrar_edats(a)"""

def llegir_llista():
    a = '1'
    b = []
    while a != 'fi':
        a= input("Introdueix una llista entera i posa 'fi' per aturar: ")
        if a != 'fi':
            b.append(a)
        else:
            return b

def filtrar_noms(l):
    a= []
    b= []
    d= ('a','e','i','o','u')
    q= ('q','w','r','t','y','p','s','d','f','g','h','j','k','l','ñ','z','c','v','b','n','m')
    for e in l:
        x=e.lower()
        if x[0] in d:
            a.append(e)
        elif x[0] in q:
            b.append(e)
    print("Els nombres que comencen amb vocal son {} i els que no son {}".format(a,b))

#PPrincipal 
a = llegir_llista()
filtrar_noms(a)