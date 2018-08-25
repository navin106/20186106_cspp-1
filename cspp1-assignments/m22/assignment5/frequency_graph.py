'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	'''
	freq graph of the dictionary
	'''
    sort_keys = sorted(dictionary)
    for i in sort_keys:
        print(i, '-', '#'*dictionary[i])
    return '\n'

def main():
	'''
	main function to read and send dictionary
	'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
