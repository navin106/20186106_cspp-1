'''
    Tiny Search Engine - Part 1 - Build a search index
    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/k appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the k occuring in the document.
    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords
def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    clean_list = ((re.sub(r'[^\w\s]', '', text)).lower()).split()
    return clean_list
def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''
    req_list = []
    for i in range(len(docs)):
        req_list.append((word_list(docs[i])))
    # initialize a search index (an empty dictionary)
    search_index = {}
    stop_words = load_stopwords("stopwords.txt")
    # iterate through all the docs
    temp = 0
    for i in req_list:
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
        for k in i:
            if k not in stop_words:
        # clean up doc and tokenize to words list
                if len(k) > 1:
                    if k not in search_index:
                        search_index[k] = [(temp, i.count(k))]
                    else:
                        # add or update the words of the doc to the search index
                        if (temp, i.count(k)) not in search_index[k]:
                            search_index[k].append((temp, i.count(k)))
                    '''
                    if k not in search_index:
                        #if temp != search_index[k][len(search_index[k])][0]:
                            t_0 = (temp, 1)
                            m = []
                            m.append(t_0)
                            search_index[k] = m
                    else:
                        #temp2 = search_index[k][len(search_index[k])-1][1]
                        temp2 += 1
                        t_1 = (temp, temp2)
                        search_index[k].append(t_1)
                    '''   
        temp += 1
        # add or update the words of the doc to the search index
    # return search index
    '''
    for i in search_index:
        count = 1
        if len(search_index[i]) > 1:
            for j in range(len(search_index[i])-1):
                if search_index[i][j] == search_index[i][j+1]:
                    count += 1
        print(count)
    '''
    return search_index
# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])
# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1
    # call print to display the search index
    print_search_index(build_search_index(documents))
if __name__ == '__main__':
    main()
