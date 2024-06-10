def round_value(s):
    "Rounded representation of the number presented in the string."
    f = float(s)        # converting the string to float
    i = int(f + .5)     # converting in integer
    return str(i)

f_src = input("Enter the name of the source file to open: ")
f_dst = input("Enter the name of the destination file to open: ")

fs = open(f_src, 'r')
fd = open(f_dst, '+a')

while 1:
    line = fs.readline()
    if line == "" or line =='\n':
        break
    line = round_value(line)
    fd.write(line + '\n')

fd.close()
fs.close()