from math import sqrt

a = float(input("Enter the lenght of the side a: "))
b = float(input("Enter the lenght of the side b: "))
c = float(input("Enter the lenght of the side c: "))

semi_perimeter = (a + b + c) / 2
area = sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))

print("The sides provides are: ", a, b, c)
print("The perimeter is: ", semi_perimeter * 2)
print("The area is: ", area)