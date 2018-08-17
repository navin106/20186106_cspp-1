'''
@author:navin106
activity 1 module 16
Document Distance - A detailed description is given in the PDF
'''
import re
import math
def clean_string(string):
    '''
    send only alphabetics words without punctuations
    '''
    string = string.replace('\'','')
    string =string.strip()
    clean_list = ((re.sub(r'[^\w\s]', '', string)).lower()).split()
    return clean_list
def vector_dictionary(new_list1, new_list2):
    '''
    creating the new dictionary
    '''
    new_dict1 = {}
    new_dict2 = {}
    big_dict = {}
    stop_words = load_stopwords("stopwords.txt")
    for i in new_list1:
        if i not in stop_words and i not in '1234567890' and len(i) != 0:
            if i not in new_dict1:
                new_dict1[i] = 1
            else:
                new_dict1[i] += 1
    for i in new_list2:
        if i not in stop_words and i not in '1234567890' and len(i) != 0:
            if i not in new_dict2:
                new_dict2[i] = 1
            else:
                new_dict2[i] += 1
    for i in new_dict1 and new_dict2:
        big_dict[i] = [new_dict1[i], new_dict2[i]] 
    for i in new_dict1:
        if i not in big_dict:
            big_dict[i] = [new_dict1[i], 0]
    for i in new_dict2:
        if i not in big_dict:
            big_dict[i] = [0, new_dict2[j]]
    '''
    for i in new_dict1:
        if i not in new_dict2:
            big_dict[i] = [new_dict1[i], 0]
        else:
            big_dict[i] = [new_dict1[i], new_dict2[i]]
    for j in new_dict2:
        if j not in new_dict1:
            big_dict[j] = [0, new_dict2[j]]
        else:
            big_dict[j] = [new_dict1[j], new_dict2[j]]
    '''
    return big_dict
def similarity(string_1, string_2):
    '''
        Compute the document distance as given in the PDF
    '''
    num_erator = 0
    de_nominator1 = 0
    de_nominator2 = 0
    final_result = 0
    new_list1 = clean_string(string_1)
    new_list2 = clean_string(string_2)
    comb_dict = vector_dictionary(new_list1, new_list2)
    for i in comb_dict:
        num_erator = num_erator + comb_dict[i][0]*comb_dict[i][1]
    for i in comb_dict:
        de_nominator1 = de_nominator1 + comb_dict[i][0]**2
        de_nominator2 = de_nominator2 + comb_dict[i][1]**2
    final_result = num_erator/(math.sqrt(de_nominator1)*math.sqrt(de_nominator2))
    return final_result
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename1:
        for line in filename1:
            stopwords[line.strip()] = 0
    return stopwords
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1, input2))
if __name__ == '__main__':
    main()
