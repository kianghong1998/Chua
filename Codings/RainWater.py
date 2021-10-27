import math
inches_str = input ("How many inches of fain have fallen: ")
inches_int = int(inches_str)
volume = (inches_int/12)*43560
gallons = volume*7.48051945
print (inches_int, "in. rain on 1 arce is ", gallons, "gallons")
inches_float = float(inches_str)
print (inches_float, "in. rain on 1 arce is ", gallons, "gallons")
