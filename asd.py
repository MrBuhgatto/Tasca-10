#a = [3,[1,3], [4, 5, 6], 7, "hola", '0',0,1]

a='e'
if a == 'b':
    print('a és b')
elif a == 'c':
    print('a és c')
elif a == 'd':
    print('a és d')
elif a == 'e':
    print('a és e')
else:
    print('a no val res')

match a:
    case 'b':
        print('a és b')
    case 'c':
        print('a és c')
    case 'd':
        print('a és d')
    case 'e':
        print('a és e')
    case other:
        print('a no val res')