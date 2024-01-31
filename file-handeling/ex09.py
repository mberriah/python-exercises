def multiplication_table(_table):
    "Function that generate the table of multiplication by n (20 terms)."
    i, s = 1, ''
    while i < 20:
        s = s + str(i * _table) + " "
        i += 1
    return s


filename = input("Enter the name of the file to create: ")
f = open(filename, 'w')

table = 2
while table < 31:
    f.write(multiplication_table(table) + '\n')
    #print(multiplication_table(table) + '\n')
    table += 1
f.close()