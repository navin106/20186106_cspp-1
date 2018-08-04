# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
 x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
	print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
	numGuesses += 1
if ans**2 < x:
	low = ans
else:
	high = ans
	ans = (high + low)/2.0
	print('numGuesses = ' + str(numGuesses))
	print(str(ans) + ' is close to square root of ' + str(x))

if __name__== "__main__":
	main()
