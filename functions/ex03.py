def maximum(n1, n2, n3):
    "Returns the highest value"
    if(n1 >= n2 and n1 >= n3):
        return n1
    elif(n2 >= n1 and n2 >= n3):
        return n2
    else:
        return n
print(maximum(2, 5, 4))