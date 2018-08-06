'''
@author : navin106
# Exercise: eval quadratic
# Write a Python function, evalQuadratic(a, b, c, x), \
that returns the value of the quadratic a . x 2 + b . x + c
# This function takes in four numbers and returns a single number.
'''
def eval_quadratic(a_quad, b_quad, c_quad, x_quad):
    '''
    returing quadratic value
    '''
    return a_quad*x_quad*x_quad + b_quad*x_quad +c_quad
def main():
    '''
    calling quadratic expression
    '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for x_mfun in range(len(data)):
        temp = str(data[x_mfun]).split('.')
        if temp[1] == '0':
            data[x_mfun] = int(float(str(data[x_mfun])))
        else:
            data[x_mfun] = data[x_mfun]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))
if __name__ == "__main__":
    main()
