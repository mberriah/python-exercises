str = "sergelavalegres"
i = 0
flag = 0

for i in range(len(str) // 2):
    print(str[i], " - ", str[-i - 1])
    if(str[i] != str[-i - 1]):
        flag = 1
        break

print("The string '", str, "' ", sep='', end='')
if(flag == 0):
    print("is a palindrome.")
else:
    print("is not a palindrome")