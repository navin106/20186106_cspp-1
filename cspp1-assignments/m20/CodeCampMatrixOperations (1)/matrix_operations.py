'''
@author:navin106
matrix operations
'''
def mult_matrix(mat_1, mat_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(mat_1[1]) == len(mat_2):
        result = [[sum(x * y for x, y in zip(m1_row, m2_col)) for m2_col in zip(*mat_2)] \
        for m1_row in mat_1]
        return result
    return None
def add_matrix(mat_1, mat_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    k = [i + j for x, y in zip(mat_1, mat_2) for i, j in zip(x, y)]
    if len(mat_1[0]) == len(mat_2[0]):
        return [k[x:x+len(mat_1[1])] for x in range(0, len(k), len(mat_1[1]))]
    return None
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    flag = 0
    inp_list = input().split(',')
    rows = int(inp_list[0])
    #columns = int(inp_list[1])
    matrix = []
    for _ in range(int(rows)):
        temp_l = input().split(' ')
        if len(temp_l) == rows:
            matrix.append([int(i) for i in temp_l])
        else:
            matrix.append([int(i) for i in temp_l])
            flag = 1
    # if flag == 1:
    # 
    #     # return (matrix, 0)
        # break
    return (matrix, flag)
def main():
    '''
    calling functions
    '''
    mat_1 = read_matrix()
    mat_2 = read_matrix()
    # if isinstance(mat_1, tuple):
    #     mat_1 = mat_1[0]
    # if isinstance(mat_2, tuple):
    # mat_2 = mat_2[0]
    if (mat_1[1] or mat_2[1]) == 1:
        print("Error: Invalid input for the matrix")
        break
    if add_matrix(mat_1, mat_2) is None:
        print('Error: Matrix shapes invalid for addition')
        print(None)
    else:
        print(add_matrix(mat_1, mat_2))
    if mult_matrix(mat_1, mat_2) is None:
        print('Error: Matrix shapes invalid for mult')
        print(None)
    else:
        print(mult_matrix(mat_1, mat_2))
if __name__ == '__main__':
    main()
