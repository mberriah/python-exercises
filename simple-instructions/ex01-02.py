# Convert degrees -> radians
# An angle of 1 radian is an angle that corresponds to a portion
# of circumference equal in length to the radius.
# Since the circumference is 2 ft R, an angle of 1 radian corresponds to 
# 360° / 2 pi , or 180° / pi

# Angle provided in the begining
PI = 3.14159265359 

deg = 32
min = 13
sec = 49

# Converting seconds into fractions of a minute
fraction_of_minute = sec / 60

# Converting minutes to a fraction of a degree
fraction_of_degree = (min + fraction_of_minute)

# Angle value in decimal degrees
angle = deg + fraction_of_degree

# Radian in degree
radian = 180 / PI

# Convert angle to radians
angle_to_radian = angle / radian

print(deg, "°", min, "'", sec, "'' =", angle_to_radian, "randian(s)")
