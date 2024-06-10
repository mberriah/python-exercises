def table_multiplication(n):
    "Function that generates the multiplication talbes from 2 to 30 (20 terms)"
    i, s = 0, ""
    while i < 20:
        i = i + 1
        s = s + str(i * n) + " "
    return s


file = input("Enter the name of the file to create: ")
f = open(file, 'w')

# Tables from 2 to 30
table = 2
while table < 31:
    f.write(table_multiplication(table) + '\n')
    table = table + 1
f.close()