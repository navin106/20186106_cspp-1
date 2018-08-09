'''
#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to\
 the entry with the largest number of values associated \
with it. If there is more than one such entry, return any one of the matching keys.
'''
def biggest(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxi = 0
    ans = 0
    for i in a_dict:
        if type(a_dict[i]) == list or type(a_dict[i]) == tuple:
            if len(a_dict[i])> maxi:
                maxi = len(a_dict[i])
                ans = i
        if (maxi == 0 and ans == 0):
            maxi = 1
            ans = i
    return ans,maxi
def main():
    a_dict = {'3':1, '4':2.045, '5':'string'}
    b_dict = {'1':[1, 2, 3, 4], '3':1, '2':(2, 3, 4, 5, 6), '4':2.045, '5':'string'}
    '''
    s=input()
    l=s.split()
    if l[0][0] not in a_dict:
        a_dict[l[0][0]]=[l[1]]
    else:
        a_dict[l[0][0]].append(l[1])
    '''    
    print(biggest(a_dict))
    print(biggest(b_dict))
if __name__ == "__main__":
    main()