file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")
file3 = input("Enter the third file name: ")

f1 = open(file1, 'r')
f2 = open(file2, 'r')
f3 = open(file3, 'a')

while 1:
    line1 = f1.readline()
    line2 = f2.readline()
    if (line1 == '' and line2 == ''):
        break
    if (line1 != ''):
        f3.write(line1)
    if (line2 != ''):
        f3.write(line2)

f1.close()
f2.close()
f3.close()