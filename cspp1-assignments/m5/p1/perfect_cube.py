'''# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm
# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube
'''
def main():
   '''
    # input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here
  '''  
S = int(input())
K = S//2 +1
FLAG = 0
for i in range(K):
    if i**3 == S:
        FLAG = 1
if FLAG == 1:
    print(S, 'is a perfect cube')
else:
    print(S, 'is not a perfect cube')
            
if __name__ == "__main__":
    main()
