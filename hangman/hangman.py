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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in lettersGuessed:
        if i in secretWord:
            return True
        else:
            return False
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    length = len(secretWord)
    answer = list(length* ("_ "))
    #print(len(secretWord))
    #print(len(lettersGuessed))
    for i in lettersGuessed:
        for j in range(len(secretWord)):
            if i in secretWord[j]:
                answer[j] = secretWord[j]
            else:
                continue
    print("".join(answer))


    # FILL IN YOUR CODE HERE...
def inputRepeated(input, letterGuessed):
    if input in letterGuessed:
        return True
        print(input)
        print(letterGuessed)
    else:
        return False
        print(input)
        print(letterGuessed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
    for i in lettersGuessed:
        if i in list(available):
            available.remove(i)
    an = "".join(available)
    return an
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    count = 8
    letterGuessed = []
    print("Welcome To Hangman Game!\n")
    initial = ""
    print("I am thinking of a word that is" + str(len(secretWord)) + "long")
    print("Available letters:" + getAvailableLetters(initial))
    initial = input("Please guess a letter:")
    letterGuessed.append(initial)
    letter_string = "".join(letterGuessed)
    while count != 0 and letter_string != secretWord:
        print("You have" + str(count) + "guesses")
        initial = input("Please guess a letter:")
        letterGuessed.append(initial)
        guess =  isWordGuessed(secretWord, initial)
        repeat = inputRepeated(initial, letterGuessed)
        if guess == True and repeat != True:
            print("Good Guess:")
            getGuessedWord(secretWord,letterGuessed)
        elif guess == True and repeat == True:
            print("That letter has been repeated:")
            getGuessedWord(secretWord,letterGuessed)
        else:
            print("Oops that letter is not in my word:")
            getGuessedWord(secretWord,letterGuessed)
            count -= 1
    if letter_string == secretWord:
        print("Good Job!") + getGuessedWord(secretWord, letterGuessed)
    else:
        print("Sorry, Game Over! Please try again")
        print(secretWord)










# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
