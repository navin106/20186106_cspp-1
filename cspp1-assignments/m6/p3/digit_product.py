'''
Given a  number int_input, find the product of all the digits
example:
    input: 123
    output: 6
'''
def main():
    '''
Read any number from the input, store it in variable int_input.
'''
INT_INPUT = int(input())
PRO = 1
REM = 0
TEMP_INT = INT_INPUT
if INT_INPUT != 0:
    if TEMP_INT < 0:
        TEMP_INT = abs(TEMP_INT)
    while TEMP_INT > 0:
        REM = TEMP_INT%10
        PRO = PRO*REM
        TEMP_INT = TEMP_INT//10
    if INT_INPUT < 0:
        print(-PRO)
    else:
        print(PRO)
else:
    print(INT_INPUT)
if __name__ == "__main__":
    main()
