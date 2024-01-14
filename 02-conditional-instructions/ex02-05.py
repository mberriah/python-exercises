number_of_seconds = 12345678912

seconds_in_a_minute = 60
seconds_in_a_hour = 3600
seconds_in_a_day = 86400 # 3600 * 24
seconds_in_a_month = 2592000 # 3600 * 24 * 30
seconds_in_a_year = 31536000 # 3600 * 24 * 365

# Number of years
years = number_of_seconds // seconds_in_a_year
rest = number_of_seconds % seconds_in_a_year

# Number of months
months = rest // seconds_in_a_month
rest = rest % seconds_in_a_month

# Number of days
days = rest // seconds_in_a_day
rest = rest % seconds_in_a_day

# Number of hours
hours = rest // seconds_in_a_hour
rest = rest % seconds_in_a_hour

# Number of minutes
minutes = rest // seconds_in_a_minute
rest = rest % seconds_in_a_minute

# Number of seconds
seconds = rest

print("Converting", number_of_seconds, "in years, months, days, hours, minutes, seconds...")
print(years, "year(s)", months, "month(s)", days, "day(s)", hours, "hour(s)", minutes, "minute(s)", seconds, "second(s).")
