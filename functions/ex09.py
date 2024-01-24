def change_char(str, char1, char2, start=0, end=-1):
    "Replaces all characters 'char1' with 'char2' in the string 'str'."
    if(end == -1):
        end = len(str)
    i = 0
    s = ''
    while(i < len(str)):
        if((i >= start) and (i <= end) and (str[i] == char1)):
            s = s + char2
        else:
            s = s + str[i]
        i = i + 1
    return s
            


phrase = 'Ceci est une toute petite phrase.'
print(change_char(phrase, ' ', '*'))
print(change_char(phrase, ' ', '*', 8, 12))
print(change_char(phrase, ' ', '*', 12))
print(change_char(phrase, ' ', '*', end = 12))