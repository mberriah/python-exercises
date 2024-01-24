def elem_max(l, start=0, end=-1):
    "Returns the largest element in the list 'l'"
    if(end == -1):
        end = len(l)
    max = 0
    i = 0
    while(i < len(l)):
        if(i >= start and i <= end and l[i] > max):
            max = l[i]
        i = i + 1
    return max

serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]  
print(elem_max(serie))  
print(elem_max(serie, 2, 5))  
print(elem_max(serie, 2))   
print(elem_max(serie, end =3, start =1))