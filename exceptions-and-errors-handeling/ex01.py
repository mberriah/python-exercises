def file_exist(filename):
    "Check if a file exists or not."
    try:
        f = open(filename, 'r')
        f.close()
        return 1
    except:
        return 0

filename = input("Enter the name of the file")

if(file_exist(filename)):
    print("This file does exist.")
else:
    print("The file", filename, "cannot be found.")