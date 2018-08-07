'''
@author:navin106
'''
def payingDebtOffInAYear(balance, annualInterestRate):
	'''
	function to find fixed amount in bisection method
	'''
	mon_intrest = (annualInterestRate)/12.0
	mon_low_val = balance/12
	mon_high_val = (balance*(1 +mon_intrest)**12)/12.0
	new_bal = balance
	epsilon =0.0001
	guess = (mon_low_val+mon_high_val)/2
	while True:
		month = 1
		while (month<=12):
			new_bal = new_bal - guess
			new_bal = new_bal + (mon_intrest*new_bal)
			month = month + 1
		if new_bal > 0 and new_bal > epsilon:
			mon_low_val = guess
			new_bal = balance
		elif new_bal < 0 and new_bal < -epsilon:
			mon_high_val = guess
			new_bal = balance
		else:
			return guess
		guess = (mon_low_val + mon_high_val)/2
def main():
	'''
	calling function
	# data = "4773 0.2"
	'''
    data = input('')
    data = data.split(' ')
    data = list(map(float, data))
    print(payingDebtOffInAYear(data[0],data[1]))
    
if __name__ == "__main__":
    main()
