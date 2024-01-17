l = [32, 5, 12, 8, 3, 75, 2, 15]
even_numbers = []
odd_numbers = []
i = 0

while(i < len(l)):
    if(l[i] % 2 ==0):
        even_numbers.append(l[i])
    else:
        odd_numbers.append(l[i])
    i = i + 1

print(even_numbers)
print(odd_numbers)