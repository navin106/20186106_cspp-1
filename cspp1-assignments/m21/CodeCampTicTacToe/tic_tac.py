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
		if list(i).count('x') == 3:
			return 'x'
		else:
			if list(i).count('o') == 3:
				return 'o'
	return 'draw'
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
	# print(iscount(matrix,'x'))
	# print(iscount(matrix,'o'))
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
		print(iswinnerhorizontal(matrix))
	# elif iswinnerhorizontal(matrix) == true:
	# 	print('draw')
	# else:
	# 	print(iswinnervertical(matrix))
main()