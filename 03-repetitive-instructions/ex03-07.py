l = []
max = 0
min = 1000
sum = 0
average = 0

i = 0
while(i >= 0):
    i = eval(input("Enter the grade of the student (or -1 to stop): "))
    if(i < 0):
        print("Terminated.")
    else:
        l.append(i)

j = 0
while(j < len(l)):
    if(l[j] > max):
        max = l[j]
    if(l[j] < min):
        min = l[j]
    sum = sum + l[j]
    j = j + 1

average = sum / len(l)

print("The maximum is ", max, "the minimum is ", min, "and the average is ", average, ".", sep='')