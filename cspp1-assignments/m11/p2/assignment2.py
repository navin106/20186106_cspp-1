'''
#Exercise: Assignment-2
#Implement the update_hand function. Make sure this function has no side effects:\
 i.e., it must not mutate the hand passed in. Before pasting your function definition here,\
be sure you've passed the appropriate tests in test_ps4a.py.
'''
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    for i in word:
        if i in hand:
            hand[i] -= 1
    return hand
def main():
    '''
    calling update function
    '''
    n_input = input()
    adict = {}
    for data in range(int(n_input)):
        data = input()
        l_list = data.split()
        adict[l_list[0]] = int(l_list[1])
    data1 = input()
    print(update_hand(adict, data1))
if __name__ == "__main__":
    main()
