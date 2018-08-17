'''
@author:navin106
activity 1 module 16
    Document Distance - A detailed description is given in the PDF
'''
import re
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    new_dict1 = {}
    new_dict2 = {}
    big_dict = {}
    new_list1 = ((re.sub(r'[^\w\s]','',dict1)).lower()).split()
    new_list2 = ((re.sub(r'[^\w\s]','',dict2)).lower()).split()
    stop_words = load_stopwords("stopwords.txt")
    for i in new_list1:
    	if i not in stop_words:
    		if i not in new_dict1:
    			new_dict1[i] = 1
    		else:
    			new_dict1[i] += 1
    for i in new_list2:
    	if i not in stop_words:
    		if i not in new_dict2:
    			new_dict2[i] = 1
    		else:
    			new_dict2[i] +=1
    for i in new_dict1:
    	if i not in new_dict2:
    		big_dict[i] = [new_dict1[i],0]
    	else:
    		big_dict[i] = [new_dict1[i], new_dict2[i]]
    print(big_dict)
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
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
