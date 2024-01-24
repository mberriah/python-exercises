def name_month(n):
    "Returns the nth month of the year"
    months = ['January', 'February', 'Mars', 'April', 'May', 'June', 'July', 'Augustus', 'September', 'October', 'November', 'December']
    return months[n - 1]
    
print(name_month(4))
print(name_month(1))
print(name_month(10))
print(name_month(12))