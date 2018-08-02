'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.
'''

def main():
	'''
	# the input string is in s
	# remove pass and start your code here
	'''
	x_str = input()
	y_str = ''
	z_str = ''
	for char in x_str:
		if(z_str == ''):
			z_str = char
		elif (z_str[-1] <= char):
			z_str = z_str+char
		elif (z_str[-1] > char):
			if(len(y_str) < len(z_str)):
				y_str=z_str
				z_str=char
			else:
				z_str=char
	if (len(c) > len(y_str)):
		y_str=z_str
	print(y_str)

if __name__== "__main__":
	main()
