'''
#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl',
your program should print:

#Number of vowels: 5
'''
def main():
    '''
    # the input string is in s
    # remove pass and start your code here
    '''
    s_string = input()
    c_ount = 0
    for i in s_string:
        if i in 'aeiou':
            c_ount = c_ount+1
    print(c_ount)
if __name__ == "__main__":
    main()
