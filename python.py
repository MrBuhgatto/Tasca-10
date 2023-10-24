x= input("Introdueix primer element: " )
y= input("Introdueix segon element: " )
z= input("Introdueix tercer element: " )
if x>y:
    # x>y
    if x>y:
        # x>y i x>z
        if y>z:
            # x>y>z
            print(x, " > ", y, " > ", z)
        elif z>y:
            # x>z>y
            print(x, " > ", z, " > ", y)
        else:
            # x>y=z
            print(x, " > ", y, " = ", z)
    elif z>x:
        # z>x i x>y
        print(z, " > ", x, " > ", y)
    else:
        # x=z>y
        print(x, " = ", z, " > ", y)
elif y>x:
    # y>x
    if x>z:
        # y>x i x>z
        if y>z:
            # y>x>z
            print(y, " > ", x, " > ", z)
        elif z>x:
            # y>z>x
            print(y, " > ", z, " > ", x)
        else:
            # y>x=z
            print(y, " > ", x, " = ", z)
    elif z>y:
        # z>y i y>x
        print(z, " > ", y, " > ", x)
    else:
        # y=z>x
        print(y, " = ", z, " > ", x)
else:
    # y=x
    if x>z:
            # y=x i x>z
            print(x, " = ", y, " > ", z)
    elif z>x:
        # y=x i z>x
        print(z, " > ", x, " = ", y)
    else:
        # y=x i z=x
        print(x, " = ", y, " = ", z)
