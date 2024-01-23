str = "Hello World!"
i = 0
counter = 0

while(i < len(str)):
    if(str[i] == "e"):
        counter = counter + 1
    i = i + 1

if(counter == 1):
    print("There is one 'e' character in the string: '", str, "'.", end="")
elif(counter > 1):
    print("There are",  counter, "'e' characters in the string: '", str, "'.", end="")
else:
    print("There is no 'e' character in the string: '", str, "'", end="")