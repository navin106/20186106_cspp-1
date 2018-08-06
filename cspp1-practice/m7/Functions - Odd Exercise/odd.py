''''
@author: navin106
# Exercise: odd
# Write a Python function, odd, that takes in one number and returns True \
when the number is odd and False otherwise.
# You should use the % (mod) operator, not if.
# This function takes in one number and returns a boolean.
'''
def odd(x_odd):
    '''
    x: int or float.
    returns: True if x is odd, False otherwise
    '''
    return x_odd%2 != 0
def main():
    '''
    calling the odd function to know the number is odd or not
    '''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
