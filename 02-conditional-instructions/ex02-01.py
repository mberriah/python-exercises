year = eval(input("Enter a year: "))

if (year % 4 != 0):
    leap = 0
else:
    if year % 400 == 0:
        leap = 1
    elif year % 100 == 0:
        leap = 0
    else:
        leap = 1
if leap:
    s = 'is'
else:
    s = 'is not'
print("The year", year, s, "a leap year.")