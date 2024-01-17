l1 = ['January', 'February', 'March', 'April', 'May', 'June',
 'July', 'August', 'September', 'October', 'November', 'December']
l2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
l3 = []

i = 0
while(i < len(l1)):
    l3.append(l1[i])
    l3.append(l2[i])
    i = i + 1

print(l3)