'''
#gnuess My Number Exercise
@author = navin106
guessing game
'''
def main():
    '''
    function to find correct number
    '''
    low_n = 0
    mid_n = 50
    high_n = 100
    i = 'l'
    while i != 'c':
        print(mid_n)
        i = input("enter 'h' if gnuess is too high,\
            'l' if its too low.'c' to indicate I gnuessed correctly")
        if i == 'h':
            high_n = mid_n
            mid_n = (high_n+low_n)//2
        elif i == 'l':
            low_n = mid_n
            mid_n = (high_n+low_n)//2
    print('your gnuess number is :', mid_n)
if __name__ == "__main__":
    main()
