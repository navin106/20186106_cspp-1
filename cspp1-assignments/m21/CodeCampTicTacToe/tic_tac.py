def iswinnerhorizontal(matrix):
	for i in matrix:
		if i.count('x') == 3:
			return 'x'
		else:
			if i.count('o') == 3:
				return 'o'
	return 'draw'
def iswinnervertical(matrix):
	for i in zip(*matrix):
		if i.count('x') == 3:
			return 'x'
		else:
			if i.count('o') == 3:
				return 'o'
	return print(iswinnerhorizontal(matrix))
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
	return True
def main():
	'''
	calling function
	'''
	matrix = []
	for i in range(3):
		matrix.append(input().split())
	if isinvalid != True:
		print(isinvalid(matrix))
	else:
		print(iswinner(matrix))
main()