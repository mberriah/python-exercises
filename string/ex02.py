first_string = "Hello World!"
second_string = ""
i = 0

while(i < len(first_string)):
    second_string = second_string + (first_string[i] + '*')
    i = i + 1

print("First string: ", first_string)
print("Second string: ", second_string)