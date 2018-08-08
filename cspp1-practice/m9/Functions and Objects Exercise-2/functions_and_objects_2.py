#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(i):
	return i+1
def apply_to_each(L, f):
	k = []
	for i in L:
		k.append(inc(i))
	return k
def main():
    data = '1 -4 8 -9'#input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
