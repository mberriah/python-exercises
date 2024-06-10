file1 = input("Enter the name of the first file: ")
file2 = input("Enter the name of the seconde file: ")

f1 = open(file1, 'r')
f2 = open(file2, 'r')

c, flag, = 0, 0

while 1:
    c = c + 1
    char1 = f1.read(1)
    char2 = f2.read(1)
    if char1 == "" or char2 == "":
        break
    if char1 != char2:
        flag = 1
        break
f1.close()
f2.close()

print("Those two files", end=' ')
if flag == 1:
    print("different from character number", c)
else: 
    print("identical.")