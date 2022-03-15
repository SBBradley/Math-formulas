#Formula for calculating monthly mortgage payments.
#March 15, 2022

'''
Fixed monthly mortgage formula:
monthlyPayment = P * r * (1 + r)^n / [(1 + r)^n -1]

P = Outstanding loan amount
r = Effective monthly interest rate
n = Total number of months

Reference: https://www.wallstreetmojo.com/mortgage-formula/
'''

monthlyPayment, loanAmount, interestRate, numOfMonths = 0, 0, 0, 0
interestRate = interestRate / 12

#Returns monthly mortgage payment amount.
def  getMonthlyPayment(loanAmount, interestRate, numOfMonths):

    #monthlyPayment = P * r * (1 + r)^n / [(1 + r)^n -1]
    monthlyPayment = ((loanAmount * (interestRate * ((1 + interestRate) ** numOfMonths))) 
                     / (((1 + interestRate) ** numOfMonths) - 1))
    print("$" + str(round(monthlyPayment, 2)))
    
getMonthlyPayment(1000000, 0.01, 120)