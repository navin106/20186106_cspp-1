'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''
def check_vertical(veri_list):
    '''
    takes the input list and returns bool
    '''
    for i in zip(*veri_list):
        for j in list(i):
            if j not in '123456789':
                return False
            if len(set(i)) != 9:
                return False
    return True
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for i  in sudoku:
        for j in i:
            if j not in '123456789':
                return False
            if len(set(i)) != 9:
                return False
    return check_vertical(sudoku)
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []
    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))
if __name__ == '__main__':
    main()
