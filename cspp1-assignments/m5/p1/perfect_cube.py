# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
	# input is captured in s
	# watch out for the data type of value stored in s
	# your code starts here
	s = int(input())
	k= s//2 +1
	flag=0
	for i in range(k):
		if i**3 == s:
			flag=1
			print(i)
	if flag ==1:
		print(s,'is a perfect cube')
	else:
		print(s, 'is not a perfect cube')
			
if __name__ == "__main__":
	main()
