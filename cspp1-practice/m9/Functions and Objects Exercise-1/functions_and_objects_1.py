'''
@author:navin106
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]
'''
def apply_to_each(L, f):
    for i in range(len(L)):
        if L[i] < 0:
            L[i] = f(L[i])
    return L
def main():
    data = '0 -1'#input()
    data = data.split(" ")
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))
if __name__ == "__main__":
    main()