'''
@author:navin106
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number \
and returns the sum of digits of given number.
# This function takes in one number and returns one number.
'''

def sumofdigits(int_num):
	'''
	n is positive Integer

	returns: a positive integer, the sum of digits of n.
	'''
	if int_num > 0:
	    return int_num%10 + sumofdigits(int_num//10)
	return 0
def main():
	'''
	calling function
	'''
	numb_a = input()
	print(sumofdigits(int(numb_a)))  

if __name__ == "__main__":
    main()
