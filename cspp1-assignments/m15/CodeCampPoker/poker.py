'''
@author:navin106
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
VAL_DICT = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,\
     '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def face_values(hand):
    face_values = []
    for i in hand:
        face_values.append(VAL_DICT[i[0]])
    return face_values
def suit_values(hand):
    suit_values = []
    for i in hand:
        suit_values.append(i[1])
    return suit_values
def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    list_k = []
    list_k.append(face_values(hand).sort())
    for k in range(len(list_k)-1):
        if list_k[k+1]-list_k[k] != 1:
            return False
    return True
def is_four(hand):
    '''
    checks weather it is a four of a kind or not and sends the true or false
    '''
    list_k = []
    count = 0
    list_k.append(face_values(hand).sort())
    for k in range(len(list_k)-1):
        if list_k[k+1]-list_k[k] == 0:
            count += 1
    return count == 3
def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    l = 0
    for i in suit_values:
        l += ord(i)
    if l == 5*ord(i):
        return True
    return False
def is_three(hand):
    '''
    check weather the given hand is three of a kind
    '''
    list_k = []
    count1 = 0 
    list_k.append(face_values(hand).sort())
    for k in range(len(list_k)-1):
        if list_k[k+1]-list_k[k] == 0:
            count1 += 1
    return count1 == 2
def is_two(hand):
    '''
    check weather the given hand is a pair
    '''
    list_k = []
    list_k.append(face_values(hand).sort())
    for k in range(len(list_k)-1):
        if list_k[k+1]-list_k[k] == 0:
            count2 += 1
    return count2 == 1
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flus
    # check for straight, flush and straight flush
    if is_straight(hand) and is_flush(hand):
        retur = 7
    elif is_four(hand):
        retur = 6
    elif is_three(hand) and is_two(hand):
        retur = 5
    # best hand of these 3 would be a straight flush with the return value 3
    elif is_flush(hand):
        retur = 4
    # the second best would be a flush with the return value 2
    elif is_straight(hand):
        retur = 3
    elif is_three(hand):
        retur = 2
    elif is_two(hand):
        retur = 1
    else:
        retur = 0
    return retur
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.
        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation
        Output: Return the winning poker hand
    '''
    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)
if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
