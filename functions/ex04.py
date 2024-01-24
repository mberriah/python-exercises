def count_char(c, str):
    "Count how many times the character 'c' is in the setence 'str'."
    counter = 0
    i = 0
    while(i < len(str)):
        if(c == str[i]):
            counter = counter + 1
        i = i + 1
    return counter

print(count_char('e', 'This sentence is an example'))