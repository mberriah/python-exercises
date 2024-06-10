def search(s):
    "Search for the zip code in the string."
    i, flag, counter = 0, 0, 0
    new_string = ""
    while i < len(s):
        if s[i] == "#":
            counter = counter + 1
            if counter == 5:
                flag = 1
            elif counter == 4:
                break
        elif flag == 1:
            new_string = new_string + s[i]    
        i = i + 1
    return new_string


file = input("Enter the name of the file: ")
zip_code = input("Enter the ZIP code to search for: ")

f = open(file, 'r')
while 1:
    line = f.readline()
    if line == "":
        break
    if search(line) == zip_code:
        print(line)
f.close()