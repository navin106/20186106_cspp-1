'''
@author: navin106
'''
def iswinnerdiagonal(matrix):
    '''
    check diagonal
    '''
    r_d = []
    l_d = []
    temp = len(matrix)
    for i in range(temp):
        r_d.append(matrix[i][i])
        l_d.append(matrix[i][len(matrix)-i-1])
    if r_d.count('x') == 3:
        print('x')
        return False
    elif r_d.count('o') == 3:
        print('o')
        return False
    elif l_d.count('x') == 3:
        print('x')
        return False
    else:
        if l_d.count('x') == 3:
            print('x')
            return False
    return True
def iswinnerhorizontal(matrix):
    '''
    check horizontal
    '''
    for i in matrix:
        if i.count('x') == 3:
            print('x')
            return False
        else:
            if i.count('o') == 3:
                print('o')
                return False
    return iswinnervertical(matrix)
def iswinnervertical(matrix):
    '''
    check vertical
    '''
    a = [0]
    b = [0]
    a = [ 'x' for i in zip(*matrix) if list(i).count('x') == 3]
    b = [ 'o' for i in zip(*matrix) if list(i).count('o') == 3]
    if a[0] == 'x':
        # print('a comp')
        print('x')
        return False
    if b[0] == 'o':
        # print('b comp')
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
    for _ in matrix:
        for j in _:
            if j not in 'xo.':
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
