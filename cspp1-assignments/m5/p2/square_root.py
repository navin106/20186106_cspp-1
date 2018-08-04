# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''
    function to find the \
    square root in approximation method
    '''
    guess = 0
    epsilon = 0.01
    step = 0.1
    squrt = int(input())
    while guess <= squrt:
        if abs(guess**2 - squrt) < epsilon:
            break
        else:
            guess = guess + step
    print(str(guess))

if __name__ == "__main__":
    main()
