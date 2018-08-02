'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''
def main():
	'''
	# the input string is in s
	# remove pass and start your code here
	'''
	s_str = input()
	c_len = len(s_str)
	i_lo = 0
	k_co = 0
	for i_lo in range(k_co):
		if s_str[i_lo:i_lo+3] == 'bob':
			k_co = k_co+1
	print(k_co)
if __name__== "__main__":
	main()
