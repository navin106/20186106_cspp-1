'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def clean_string(string):
    '''
    removing special characters for string
    '''
    return (((re.sub(r'[^\w\s]', '', string))).split())
def tokenize(string):
    '''
    takes list and returns dictionary
    '''
    freq_dict = {}
    for i in string:
        freq_dict[i] = string.count(i)
    return freq_dict            
def main():
    '''
    main function to print dictonary
    '''
    temp_list = []
    no_of_lines = int(input())
    for _ in range(no_of_lines):
        temp_list.append(input())
    #for i in range(no_of_lines):
    print(tokenize(clean_string(temp_list)))

if __name__ == '__main__':
    main()
