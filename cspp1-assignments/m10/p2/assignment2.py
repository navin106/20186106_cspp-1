# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secret_word, lettersguessed):
    '''
    secret_word: string, the word the user is guessing
    lettersguessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in lettersguessed;
      False otherwise
    '''
    count = 0
    for i in secret_word:
        if i in lettersguessed:
            return True
    return False


def getGuessedWord(secret_word, lettersguessed):
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



def getAvailableLetters(lettersguessed):
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
    user_input = ""
    backup = []
    while True:
        print("-----------")
        print("You have " +  str(wrong_count) +" guesses left.")
        print("Available letters: " + getAvailableLetters(user_input.split()))
        char_entered = input("Please guess a letter: ")
        user_input = user_input + ' ' +char_entered
        if char_entered not in backup:
            if isWordGuessed(secret_word, char_entered):
                print("Good guess: " + getGuessedWord(secret_word, user_input.split()))
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secret_word, user_input.split()))
                wrong_count -= 1
        else:
            print('Oops! Youve already guessed that letter:'+ getGuessedWord(secret_word, user_input.split()))
        backup = backup +user_input.split()
        if getGuessedWord(secret_word, user_input.split()) == secret_word:
            print("Congratulations, you won!")
            break
        elif wrong_count == 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word)
            break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secret_word while you're testing)

secret_word = chooseWord(wordlist).lower()
hangman(secret_word)
