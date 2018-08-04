# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
	'''
	# epsilon and step are initialized
	# don't change these values
	'''
	s = int(input())
	epsilon = 0.01
	lower = 0.0
	high = s
	mid = (low+high)/2.0
	while abs(mid**2-num) > epsilon:
		if mid**2 < s:
			lower = mid
		else:
			high = mid
		mid = (lower+high)/2.0
	print(mid)	
if __name__== "__main__":
	main()
