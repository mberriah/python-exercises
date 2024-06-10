def encode():
    "Return the list of the values entered or an empty list."
    print("Enter the data (or 'Enter' to close): ")

    while 1:
        name = input("Name: ")
        if name == "":
            return []
        firstname = input("First name: ")
        birth = input("Date of birth: ")
        sex = input("Sex: ")
        adress = input("Adress: ")
        zip_code = input("Zip code: ")
        city = input("City: ")
        tel = input("Telefon number: ")
        print(name, firstname, adress, zip_code, city)
        
        check = input("Enter 'Enter' if it is ok or 'n' otherwise.")

        if check == "":
            break
    return [name, firstname, adress, zip_code, city, tel]

def register(l):
    "Register the data list separated with '#'."

    i = 0
    while i < len(l):
        f.write(l[i] + '#')
        i = i + 1
    f.write("\n")

file = input("Enter the destination file: ")
f = open(file, 'a')
while 1:
    list = encode()
    if list == []:
        break
    register(list)

file.close()