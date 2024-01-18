year = eval(input("Enter a year: "))

if((year % 4 ==0) and ((year % != 100) or (year % 400 == 0))):
    leap = 1
else: 
    leap = 0

if leap:
    s = 'is'
else:
    s = 'is not'
print("The year", year, s, "a leap year.")
