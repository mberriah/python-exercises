file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")

f1 = open(file1, 'r')
f2 = open(file2, 'r')

i, flag = 0, 0

while 1:
    i += 1
    char1 = f1.read(1)
    char2 = f2.read(1)
    if (char1 == '' or char2 == ''):
        break
    elif (char1 != char2):
        flag = 1
        break

f1.close()
f2.close()

print("Those tow files ", end= '')
if flag == 1:
    print("are different from character: ", i, ".", sep='')
else:
    print("are identical.", sep='')