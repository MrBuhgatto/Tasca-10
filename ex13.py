# Exercici 13: Definir una funció gran() que, donats dos números, retorni el major.  Prova-la amb diferents exemples.
def major(n,m):
    if n>m:
        return n
    else:
        return m
a= int(input('Intro el 1r numero: '))
b= int(input('Intro el 2r numero: '))
c= major(a,b)
print('El major de {} i {} és {}'. format(a,b,c))
