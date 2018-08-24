'''
@author: navin106
'''
def iswinnerdiagonal(matrix):
    '''
    check diagonal
    '''
    temp = len(matrix)
    r_d = [matrix[i][i] for i in range(temp)]
    l_d = [matrix[i][temp-i-1] for i in range(temp)]
    if r_d.count('x') == 3 or l_d.count('x') == 3:
        print('x')
        return False
    if r_d.count('o') == 3 or l_d.count('o') == 3:
        print('o')
        return False
    return True
def iswinnerhorizontal(matrix):
    '''
    check horizontal
    '''
    if ['x' for i in matrix if i.count('x') == 3] == ['x']:
        print('x')
        return False
    if ['o' for i in matrix if i.count('o') == 3] == ['o']:
        print('o')
        return False
    return iswinnervertical(matrix)
def iswinnervertical(matrix):
    '''
    check vertical
    '''
    if ['x' for i in zip(*matrix) if list(i).count('x') == 3] == ['x']:
        print('x')
        return False
    if ['o' for i in zip(*matrix) if list(i).count('o') == 3] == ['o']:
        print('o')
        return False
    return iswinnerdiagonal(matrix)
def iscount(matrix, chk_chr):
    '''
    returns sum of count of the char
    '''
    k = []
    for i in matrix:
        k.append(i.count(chk_chr))
    return sum(k)
def isinvalid(matrix):
    '''
    return bool for input is valid or not
    '''
    if ['f' for i in matrix for j in i if j not in 'xo.'] == ['f']:
        print('invalid input')
        return False
    if iscount(matrix, 'x') > 5 or iscount(matrix, 'o') > 5 or \
    (iscount(matrix, 'x') == 3 and iscount(matrix, 'o') == 3):
        print('invalid game')
        return False
    return True
def main():
    '''
    calling function
    '''
    matrix = []
    for _ in range(3):
        matrix.append(input().split())
    if isinvalid(matrix):
        if iswinnerhorizontal(matrix):
            print('draw')
main()
