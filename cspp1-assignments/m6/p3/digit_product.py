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
int_input = int(input())
pro =1
rem =0
temp_int = int_input
if int_input!=0:
    if temp_int<0:
        temp_int=abs(temp_int)
    while temp_int>0:
        rem =temp_int%10
        pro = pro*rem
        temp_int = temp_int//10
    if int_input<0:
        print(-pro)
    else:
        print (pro)
else:
    print(int_input)
if __name__ == "__main__":
    main()
