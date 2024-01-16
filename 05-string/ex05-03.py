string = "zorglub"
inverted_string = ""
i = len(string) - 1

while(i >= 0):
    inverted_string = inverted_string + string[i]
    i = i - 1

print("First string: ", string)
print("Inverted string: ", inverted_string)