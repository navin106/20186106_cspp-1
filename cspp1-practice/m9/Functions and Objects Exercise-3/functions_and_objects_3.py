#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]
def square(i):
    return i**2
def apply_to_each(L, f):
    k =[]
    for i in L:
        k.append(f(i))
    return k    
def main():
    data = '1 -4 8 -9'#input()
    data = data.split(" ")
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__== "__main__":
    main()