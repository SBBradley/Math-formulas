#Example of pythagorean theorem.
#March 8, 2022

'''
Pythagorean theorem:
a^2 + b^2 = c^2
'''
import math
a, b, c = 0, 0, 0

#Calculates the pythagorean theorem of the parameters.
def pyTheorem(a, b):
    c = math.sqrt((a**2) + (b**2))
    print(round(c, 1))

pyTheorem(1, 2)