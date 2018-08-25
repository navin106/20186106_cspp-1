'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    '''
    main function to write and read input
    '''
    temp_list = []
    no_of_lines = int(input())
    for _ in range(no_of_lines):
        temp_list.append(input())
    for i in range(no_of_lines-1):
        print(temp_list[i])

if __name__ == '__main__':
    main()
