def triple_space(_line):
    "Triple the number of space of a string."
    i, s = 0, ""
    while (i < len(_line)):
        if (_line[i] == " "):
            s = s + _line[i] * 3
        else:
            s = s + _line[i]
        i += 1
    return s

source_file = input("Enter the source file name to copy from: ")
destination_file = input("Enter the destination file name to copy to: ")

fsrc = open(source_file, 'r')
fdst = open(destination_file, "w")

lines = fsrc.readlines()

for line in lines:
    print(line)
    fdst.write((triple_space(line)))

fsrc.close()
fdst.close()