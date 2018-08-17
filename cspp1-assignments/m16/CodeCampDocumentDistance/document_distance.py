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
    d = 0
    new_dict1 = {}
    new_list1 = ((re.sub(r'[^\w\s]','',dict1)).lower()).split()
    new_list2 = ((re.sub(r'[^\w\s]','',dict2)).lower()).split()
    stop_words = load_stopwords("stopwords.txt")
    for i in new_list1:
    	if i not in stop_words:
    		d += 1
    		new_dict1[i] = d
    print(new_dict1)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    print(stopwords)
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
