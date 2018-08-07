'''
@author:navin106
fixed monthly payment by using bisection method.
'''
def paydebt_year(blance_inp, annual_intrest_rate):
    '''
    bisection method to find out fixed amount
    '''
    mon_int = (annual_intrest_rate) / 12.0
    mon_low = blance_inp / 12
    mon_high = (blance_inp * (1 + mon_int)**12) / 12.0
    new_bal = blance_inp
    epsilon = 0.03
    guess = (mon_low + mon_high)/2
    while True:
        month = 1
        while month <= 12:
            new_bal = new_bal - guess
            new_bal = new_bal + (mon_int * new_bal)
            month += 1
        if new_bal > 0 and new_bal > epsilon:
            mon_low = guess
            new_bal = blance_inp
        elif new_bal < 0 and new_bal < -epsilon:
            mon_high = guess
            new_bal = blance_inp
        else:
            return guess
        guess = (mon_low + mon_high)/2
def main():
    '''
    calling function
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", round(paydebt_year(data[0], data[1]), 2))
if __name__ == "__main__":
    main()
    