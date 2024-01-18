from sys import exit

print("Enter the length of the three sides of a triangle.")
a, b, c = eval(input())

# A triangle can only be constructed if each side 
# is less than the sum of the other two
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print("We can build a triangle.")
else:
    print("It is impossible to build a triangle.")
    exit()
    
flag = 0 
if a == b and b == c : 
    print("This triangle is equilateral.") 
    flag = 1 
elif a == b or b == c or c == a : 
    print("This triangle is isosceles.") 
    flag = 1 
if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b : 
    print("This triangle is right-angled.") 
    flag = 1 
if flag == 0 : 
    print("This triangle is any.")