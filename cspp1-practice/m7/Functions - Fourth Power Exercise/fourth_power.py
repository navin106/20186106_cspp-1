'''
@author : navin106
# Exercise: fourth power
# Write a Python function, fourthPower, that takes in one\
 number and returns that value raised to the fourth power.
# You should use the square procedure that you defined in \
an earlier exercise exercise (you don't need to redefine square in this box;
# This function takes in one number and returns one number.
'''
def square(x_power4):
    '''
    suare the given number and returns it
    x_power4: int or float.
    '''
    return x_power4*x_power4
def fourth_power(x_power4):
    '''
    square the given number and returns it
    x_power4: int or float.
    '''
    return square(x_power4)*square(x_power4)
def main():
    '''
    call the fourth_power function to get fourth power of a given number
    '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))
if __name__ == "__main__":
    main()
