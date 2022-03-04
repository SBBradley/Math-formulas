#Example of percentage formula.
percent, value, totalValue = 0, 0, 0

def getPercentage(value, totalValue):
    percent = (value / totalValue) * 100
    return int(percent)

print(getPercentage(7, 10),"%")