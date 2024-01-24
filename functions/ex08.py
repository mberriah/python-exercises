def volume_box(x1=-1, x2=-1, x3=-1):
    "Volume of a parallelepiped box"
    if(x1 == -1):               # no arguments
        return -1
    elif(x2 == -1):             # 1 arguments
        return x1 ** 3
    elif(x3 == -1):             # 2 arguments
        return (x1 ** 2) * x2
    else:
        return x1 * x2 * x3


print(volume_box())
print(volume_box(5.2))
print(volume_box(5.2, 3))
print(volume_box(5.2, 3, 7.4))