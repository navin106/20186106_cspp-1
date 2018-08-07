# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sumofdigits(n):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if n > 0:
    	return n%10 + sumofdigits(n//10)
    else:
    	return 0


def main():
    a = '234'#input()
    print(sumofdigits(int(a)))  

if __name__== "__main__":
    main()

