#Demonstrates the perimeter and area forumulas for a rectangel
#March 3, 2022

'''
p = perimeter
a = area
b = breadth (width)
l = length

Perimeter formula: p = 2(l + b)
Area formula: a = l * b

Ref: https://www.geeksforgeeks.org/basic-math-formulas/
'''
p, a, l, b = 0, 0, 0, 0

#Calculates perimeter of rectangle
def rectanglePerimeter(l, b):
    p = 2 * (l + b)
    print(int(p))

#Calculates area of rectangle
def rectangleArea(l,b):
    a = l * b
    print(int(a))

rectanglePerimeter(1, 2)
rectangleArea(3, 4)