l = [32, 5, 12, 8, 3, 75, 2, 15]
max = 0
i = 0

while(i < len(l)):
    if(l[i] > max):
        max = l[i]
    i = i + 1

print("The largest element in this list has the value:", max)