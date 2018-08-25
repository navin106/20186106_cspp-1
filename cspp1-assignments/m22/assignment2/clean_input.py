'''
@author:navin106
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''
    removing special characters for string
    '''
    return ''.join(((re.sub(r'[^\w\s]', '', string)).lower()).split())
def main():
    '''
    main function to print clean string
    '''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
