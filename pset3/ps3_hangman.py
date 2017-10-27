# Hangman game
#

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
    # Loop through secretWord
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False

    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ''

    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word += letter + " "
        else:
            guessed_word += "_ "
    return guessed_word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    alphabet = 'abcdefghijklmnopqrstuvqwxyz'
    available_letters = alphabet[:]
    for letter in lettersGuessed:
        available_letters = available_letters.replace(letter, '')
    return available_letters

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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))

    guesses_remaining = 8
    letters_guessed = []

    while not isWordGuessed(secretWord, letters_guessed):
        print("-------------")
        print("You have {} guesses left.".format(guesses_remaining))
        available_letters = getAvailableLetters(letters_guessed)
        print("Available letters: " + available_letters)

        # Assumes only letters are allowed
        new_guess = input("Please guess a letter: ")
        new_guess = new_guess.lower()

        # Guess feedback
        if new_guess in available_letters:
            # If valid guess, generate new word_status
            letters_guessed.append(new_guess)
            word_status = getGuessedWord(secretWord, letters_guessed)
            if new_guess in secretWord:
                print("Good guess: " + word_status)
            else:
                print("Oops! That letter is not in my word: " + word_status)
                guesses_remaining -= 1
        else:
            print("Oops! You've already guessed that letter: " + word_status)

        # End game if guesses run out
        if guesses_remaining == 0:
            break

    print("-------------")

    # If user won
    if isWordGuessed(secretWord, letters_guessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord)






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
