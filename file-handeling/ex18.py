file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the second file: ")
file3 = input("Enter the name of third file: ")

f1 = open(file1, 'r')
f2 = open(file2, 'r')
f3 = open(file3, 'w')

while 1:
    line1 = f1.readline()
    line2 = f2.readline()

    if line1 == "" and line2 == "":
        breqk
    
    if line1 != "":
        f3.write(line1)
    
    if line2 != "":
        f3.write(line2)

f1.close()
f2.close()
f3.close()