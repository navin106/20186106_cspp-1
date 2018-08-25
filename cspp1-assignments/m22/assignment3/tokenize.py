'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

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
    inp_word_list = input().split()
    print(tokenize(inp_word_list))

if __name__ == '__main__':
    main()
