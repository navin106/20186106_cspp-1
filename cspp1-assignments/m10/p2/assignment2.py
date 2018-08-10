'''
@author:navin106
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
'''
import random
WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # WORD_LIST: list of strings
    word_l = line.split()
    print("  ", len(word_l), "words loaded.")
    return word_l
def choose_word(w_list):
    """
    w_list (list): list of words (strings)
    Returns a word from w_list at random
    """
    return random.choice(w_list)
# end of helper code
# -----------------------------------
# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, lettersguessed):
    '''
    secret_word: string, the word the user is guessing
    lettersguessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in lettersguessed;
      False otherwise
    '''
    for i in secret_word:
        if i in lettersguessed:
            return True
    return False
def get_guessed_word(secret_word, lettersguessed):
    '''
    secret_word: string, the word the user is guessing
    lettersguessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    k = ''
    for i in secret_word:
        if i in lettersguessed:
            k = k + i
        else:
            k = k + '_'
    return k
def get_availablel_etters(lettersguessed):
    '''
    lettersguessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    a_dummy = 'abcdefghijklmnopqrstuvwxyz'
    l_new = ''
    for i in a_dummy:
        if i not in lettersguessed:
            l_new = l_new + i
    return l_new
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    wrong_count = 8
    u_inp = ""
    backup = []
    l_n = []
    while True:
        print("-----------")
        print("You have " +  str(wrong_count) +" guesses left.")
        print("Available letters: " + get_availablel_etters(l_n))
        char_entered = input("Please guess a letter: ")
        u_inp = u_inp + ' ' +char_entered
        l_n = l_n + u_inp.split()
        if char_entered not in backup:
            if is_word_guessed(secret_word, char_entered):
                print("Good guess: " + get_guessed_word(secret_word, l_n))
            else:
                print("Oops! That letter is not in my word:" + get_guessed_word(secret_word, l_n))
                wrong_count -= 1
        else:
            print('Oops! Youve already guessed that letter:'+ get_guessed_word(secret_word, l_n))
        backup = backup +l_n
        if get_guessed_word(secret_word, l_n) == secret_word:
            print("Congratulations, you won!")
            break
        elif wrong_count == 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word)
            break
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secret_word while you're testing)
SECRET_WORD = choose_word(word_list).lower()
hangman(SECRET_WORD)
