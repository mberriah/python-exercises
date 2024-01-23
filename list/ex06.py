l = ['John', 'Maximilian', 'Brigitte', 'Sonia', 'Peter', 'Sandra']

under_six_chars = []
above_six_chars = []
i = 0

while(i < len(l)):
    if(len(l[i]) < 6):
        under_six_chars.append(l[i])
    else:
        above_six_chars.append(l[i])
    i = i + 1

print(under_six_chars)
print(above_six_chars)