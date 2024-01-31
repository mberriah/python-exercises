def remove_last_char(line):
    "Returns the string except its last '\n' character."
    trimmed_line = line[:-1]
    return trimmed_line

def add_lines(file):
    "Appends string(s) in the specified file."
    f = open(file, 'a')
    while 1:
        line = input("Enter your line or 'Enter' to finish: ")
        if line == '':
            break
        else:
            f.write(line + '\n')
    f.close()

def read_file(file):
    "Reads the content of the specified file."
    try:
        f = open(file, 'r')
        while 1:
            line = f.readline()
            if line == '':
                break
            print(remove_last_char(line))
        f.close()
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    choice = ''
    filename = input("Enter the name of the file: ")

    while(choice != 'a' and choice != 'r'):
        choice = input("Type 'a' to append new lines or 'r' to read the file: ")
        if(choice != 'a' and choice != 'r'):
            print("Allowed answers: 'n' or 'r'.\nTry again.")

    if(choice == "n"):
        add_lines(filename)
    elif(choice == "r"):
        l = read_file(filename)