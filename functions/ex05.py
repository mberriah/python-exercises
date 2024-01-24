def index_max(l):
    "Returns the index of the largest element in the list."
    max = l[0]
    i, imax = 0, 0
    while(i < len(l)):
        if(l[i] > max):
            max = l[i]
            imax = i
        i = i + 1
    return imax

serie = [5, 8, 2, 1, 9, 3, 6, 7]
print(index_max(serie))