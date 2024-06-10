def triple_space(s):
    "Function that triples the spaces between each words."
    i, new_string = 0, ""
    while i < len(s):
        if s[i] == ' ':
            new_string = new_string + "   "
        else:
            new_string = new_string + s[i]
    return new_string


file = input("Enter the file to open: ")
f = open(file, 'r+')        # r+ = read and write
lines = f.readlines()

i = 0
while i < len(lines):
    lines[i] = triple_space(lines[i])
    i = i + 1

f.seek(0)                   # back to begining
f.wriltelines(lines)
f.close