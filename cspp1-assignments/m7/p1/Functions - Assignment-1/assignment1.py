'''
@author: navin106
# Functions | Assignment-1 - Paying Debt off in a Year
# Write a program to calculate the credit card balance after one year\
 if a person only pays the minimum monthly payment required by the
# credit card company each month.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal
# For each month, calculate statements on the monthly\
 payment and remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print
# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135
# So your program only prints out one thing: \
the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0
# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month =\
 (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
def paying_DebtOffInAYear(previous_balance, annual_InterestRate, monthly_PaymentRate):
    '''
    function to find final balance
    '''
    i=0
    for i in range(12):
        unpaid_balance = previous_balance - monthly_PaymentRate*previous_balance
        new_balance = unpaid_balance + (annual_InterestRate/12.0)*unpaid_balance
        i = new_balance
        previous_balance = i
    return round(i, 2)
def main():
    '''
    function to call paying debt
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print('Remaining balance:', paying_DebtOffInAYear(data[0], data[1], data[2]))
if __name__ == "__main__":
    main()
