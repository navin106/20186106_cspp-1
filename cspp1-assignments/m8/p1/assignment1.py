'''
@author:navin106
# Exercise: Assignment-1
# Write a Python function, factorial(fac_number), that takes \
in one number and returns the factorial of given number.
# This function takes in one number and returns one number.
'''
def factorial(fac_number):
    '''
    fac_number is positive Integer
    returns: a positive integer, the factorial of fac_number.
    '''
    if fac_number == 0:
        return 1
    elif fac_number == 1:
        return 1
    else:
        return fac_number*factorial(fac_number-1)
def main():
    '''
    caaling factorial function
    '''
    a = input()
    print(factorial(int(a)))
if __name__ == "__main__":
    main()
