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
    clean_string = ((re.sub(r'[^\w\s]', '', string)).lower()).split()
    return ''.join(clean_string)
def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
