def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    # print(m1)
    # print(m2)
    if len(m1[1]) == len(m2):
        result = [[sum(x * y for x, y in zip(m1_row, m2_col)) for m2_col in zip(*m2)] for m1_row in m1]
        return result
    else:
        return 'Error: Matrix shapes invalid for mult'
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    # for i in m1:
    #     for j in m2:
    k = [i + j for x, y in zip(m1, m2) for i,j in zip(x, y)]
    if (len(m1[0]) == len(m2[0])):
        return [k[x:x+len(m1[1])] for x in range(0,len(k),len(m1[1]))]
    else:
        print('Error: Matrix shapes invalid for addition')
def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    flag = 0
    n = input().split(',')
    rows = int(n[0])
    columns = int(n[1])
    matrix = []
    for row in range(rows):
        l = input().split(' ')
        if len(l) == rows:
            matrix.append([int(i) for i in l])
        else:
            matrix.append([int(i) for i in l])
            flag = 1
    if flag == 1:
        print("Error: Invalid input for the matrix")
        return (matrix,True)
    return matrix

def main():
    # read matrix 1
    m1 = read_matrix()
    m2 = read_matrix()
    # add matrix 1 and matrix 2
    # read matrix 2
    if type(m1) == tuple :
        # print('None')
        m1 = m1[0]
        # print(add_matrix(m1[0], m2))
        # print(mult_matrix(m1[0], m2))
    if type(m2) == tuple:
        # print('None')
        m2 = m2[0]
        # print(add_matrix(m1, m2[0]))
        # print(mult_matrix(m1, m2[0]))
    print(m1,m2)
    print(add_matrix(m1, m2))
    print(mult_matrix(m1, m2))
    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()