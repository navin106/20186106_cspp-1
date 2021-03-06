'''
@author:navin106
    Assignment-1 Create Social Network
'''
def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people
        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie
        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,
        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary
        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right
        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    l_enter = []
    k_follows = []
    m_final = []
    s_dict = {}
    l_enter = data.split('\n')
    l_revised = []
    for i in range(len(l_enter)-1):
        l_revised.append(l_enter[i])
    temp = len(l_revised)
    for i in range(temp):
        k_follows = l_revised[i].split(' follows ')
        m_final.extend(k_follows)
    if len(m_final) > len(k_follows):
        for i in range(0, len(m_final), 2):
            if m_final[i] not in s_dict:
                s_dict[m_final[i]] = m_final[i+1].split(',')
        return s_dict
    return {}
def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(create_social_network(string))
if __name__ == "__main__":
    main()


k = len(network)
        if agr1 not in network:
            network(k+1)