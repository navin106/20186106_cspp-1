'''
#Exercise : how many
# write a procedure, called how_many, which returns the sum of \
the number of values associated with a dictionary.
'''
def how_many(a_dict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    l_list = []
    for i in a_dict.values():
        if isinstance(i, list):
            l_list.extend(i)
        elif isinstance(i, tuple):
            l_list.extend(list(i))
        elif isinstance(i, (int, float)):
            l_list.append(i)
        else:
            l_list.append(0)
    print(l_list)
    return sum(l_list)
def main():
    '''
    s=input()
    l_list=s.split()
    if l_list[0][0] not in a_dict:
        a_dict[l_list[0][0]]=[l_list[1]]
    else:
        a_dict[l_list[0][0]].append(l_list[1])
    '''
    a_dict = {'1':[1, 2, 3, 4], '2':(2, 3, 4, 5), '3':1, '4':2.045, '5':'string'}
    print(how_many(a_dict))
if __name__ == "__main__":
    main()
