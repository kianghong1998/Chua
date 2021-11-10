import math

radius_str = input ("Enter the radius: ")
radius_int = int (radius_str)

circum = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

print (" the circumference is: ", circum, \
", and the area is: ", area)
