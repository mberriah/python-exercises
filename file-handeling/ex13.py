def str_without_last_char(s):
    "This function returns the string without the last character."
    new_string = ""
    i, j = 0, len(string) - 1
    while i < j:
        new_string = new_string + s[i]
        i = i + 1
    return new_string

def write():
    f = open(file, 'a')
    while 1:
        line = input("Enter a line of text (or Enter to end): ")
        if line == '':
            break
        else:
            f.write(line + '\n')
    f.close()

def read():
    f = open(file, 'r')
    while 1:
        line = f.readline()
        if line == '':
            break
        print(str_without_last_char(line))
    f.close()

file = input("Enter the file to open: ")
choice = input("Enter 'w' to write or 'r' to read the file: ")

if choice == 'w':
    read()
else: 
    read()