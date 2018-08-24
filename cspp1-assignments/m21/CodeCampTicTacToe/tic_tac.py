def iscount(matrix, chk_chr):
	'''
	returns sum of count of the char
	'''
	k = []
	for i in matrix:
		k.append(i.count(chk_chr))
	return sum(k)
def isinvalid(matrix):
	'''
	return bool for input is valid or not
	'''
	for i in matrix:
		for j in i:
			if j not in 'xo.':
				return 'invalid input'
	if iscount(matrix,'x') or iscount(matrix,'o') or iscount(matrix,'.') > 5:
		return 'invalid game'



def main():
	'''
	calling function
	'''
	matrix = []
	for i in range(3):
		matrix.append(input().split())
	print(isinvalid(matrix))
main()