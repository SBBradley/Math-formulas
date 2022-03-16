#Example of average formula.
#March 4, 2022
a, b, c, d,= 0, 0, 0, 0
average, count = 0, 0

#Calculates the average of the parameters.
def getAverage(a, b, c, d, count):
    average = (a + b + c +d) / count
    print(average)

getAverage(1, 2, 3, 4, 4)