#Example of average formula.
a, b, c, d,= 0, 0, 0, 0
average, count = 0, 0

def getAverage(a, b, c, d, count):
    average = (a + b + c +d) / count
    return average

print(getAverage(1, 2, 3, 4, 4))