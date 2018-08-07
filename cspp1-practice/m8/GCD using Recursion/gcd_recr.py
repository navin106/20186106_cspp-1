'''
@author: navin106
# Exercise: GCDRecr
# Write a Python function, gcd_recur(a, b), that takes in two\
 numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.
'''
def gcd_recur(a_int, b_int):
    '''
    a_int, b_int: positive integers 
    returns: a_int positive integer, the greatest common divisor of a_int & b_int.
    '''
    if a_int == 0 or b_int == 0:
        return 0
    elif a_int%b_int == 0:
        return b_int
    elif b_int%a_int == 0:
        return a_int
    elif a_int > b_int:
        return gcd_recur(b_int, a_int%b_int)
    else:
        return gcd_recur(a_int, b_int%a_int)
def main():
    '''
    calling function
    '''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))
if __name__ == "__main__":
    main()
