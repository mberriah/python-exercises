# Formula: A = P * (1 + r/n)**nt
# A = Accrued amount (principal + interest)
# P = Principal amount
# r = Annual nominal interest rate as a decimal
# n = number of compounding periods per unit of time
# t = time in decimal years; e.g., 6 months is calculated as 0.5 years. Divide your partial year number of months by 12 to get the decimal years.
# I = Interest amount

P = 100
r = 0.043
n = 1
t = 20
I = 0

# Calculating the interest earned each year 
i = 1
while(i < 21):
    print("Year", i, ":", float(format(P, '.2f')), "x", float(format(r * 100, '.2f')), "% = ", float(format(P * r, '.2f')), "euros.")
    I = I + (P * r)
    P = P + (P * r)
    i = i + 1
print("Cumulative interest: ", float((format(I, '.2f'))), "euros.")
