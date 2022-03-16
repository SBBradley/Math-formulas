#Example of percentage formula.
#March 4, 2022
percent, value, totalValue = 0, 0, 0

#Calculates percentage of the parameters.
def getPercentage(value, totalValue):
    percent = (value / totalValue) * 100
    #return int(percent)
    print(str(round(percent, 2)) + "%")

getPercentage(7, 10)