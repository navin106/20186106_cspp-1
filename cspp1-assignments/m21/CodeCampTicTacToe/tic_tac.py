def iswinnerhorizontal(matrix):
	for i in matrix:
		if i.count('x') == 3:
			print('x')
			return False
		else:
			if i.count('o') == 3:
				print('o')
				return False
	return True
def iswinnervertical(matrix):
	for i in zip(*matrix):
		if list(i).count('x') == 3:
			print('x')
			return False
		else:
			if list(i).count('o') == 3:
				print('o')
				return False
	return True
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
				print('invalid input')
				return False
			else:
				if iscount(matrix,'x') or iscount(matrix,'o') > 5:
					print('invalid game')
					return False
	return True
def main():
	'''
	calling function
	'''
	matrix = []
	for i in range(3):
		matrix.append(input().split())
	if isinvalid(matrix):
		if iswinnerhorizontal(matrix):
			if iswinnervertical(matrix):
				print(iswinnerhorizontal(matrix))
main()