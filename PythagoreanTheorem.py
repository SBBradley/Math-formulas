import math

#Example of pythagorean theorem.
a, b, c = 0, 0, 0

#a^2 + b^2 = c^2
def pyTheorem(a, b):
    c = math.sqrt((a**2) + (b**2))
    return round(c, 1)

print(pyTheorem(1, 2))