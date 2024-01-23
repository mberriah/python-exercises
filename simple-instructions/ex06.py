miles_per_hour = float(input("Enter speed in miles/hour: "))

meters_per_second = miles_per_hour * 1609 / 3600
kilometers_per_hour = miles_per_hour * 1.609

print(miles_per_hour, "miles/hour =", meters_per_second, "m/sec.")
print(miles_per_hour, "miles/hour =", kilometers_per_hour, "km/h.")