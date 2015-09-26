__author__ = 'oanapy'

#
# Hangman game
#

# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"
HANGMANPICS = "hangman_pic.txt"
LETTERSGUESSED = []
TRIES = 0
MAX_TRIES = 0
PIC_ROW = 0


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Let's play Hangman!"
    print "Loading word list and pics from files..."

    # inFile: file
    inFileW = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    lineW = inFileW.readline()
    # wordlist: list of strings
    wordlist = string.split(lineW)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """

    global MAX_TRIES
    cuvant_secret = random.choice(wordlist)
    MAX_TRIES = len(cuvant_secret)
    return cuvant_secret

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """

    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """

    word = ''
    for char in secretWord:
        if char in lettersGuessed:
            word += char
        else:
            word += '_ '

    print word


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """

    alphabet = list(string.ascii_lowercase)

    all_letters = alphabet + lettersGuessed

    for letter in lettersGuessed:
        while letter in all_letters:
            all_letters.remove(letter)
    remainders = ''.join(all_letters)
    return remainders


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    user_choice = raw_input().lower()
    if user_choice == "yes":
        hangman(secretWord)
        return True

# load the pics from Hangman_pic file
HMfile = open(HANGMANPICS, 'r', 0)
lineHM = HMfile.readline()
HMpics = string.split(lineHM, ',')


def hangman(secretWord):
    """
    Starts up an interactive game of Hangman.
    """

    global TRIES, MAX_TRIES, PIC_ROW
    lettersGuessed = []
    condition = True
    missed_letters = []
    picRow = 0

    print "The Secret Word contains " + str(len(secretWord)) + " letters"
    print "You have %s tries!" % str(MAX_TRIES)

    if TRIES <= MAX_TRIES:
        while condition:
            # takes user input on letters
            letter = raw_input("Your guess is: ")
            # appends the user's letters and checks if letter has been entered before
            if letter in lettersGuessed:
                print "Sorry! Letter already used!"
                playAgain()
            lettersGuessed.append(letter)

            # prints the word as "_ pp _ e (apple)"
            getGuessedWord(secretWord, lettersGuessed)

            # prints a hangman image corresponding to each wrong letter
            if letter not in secretWord:
                missed_letters.append(letter)
                picRow += 1
                pics = "\n".join(HMpics[:picRow])
                print pics

            print "Your guessed letters are: " + str(lettersGuessed)
            # prints the other available letters of the alphabet
            remaining_letters = getAvailableLetters(lettersGuessed)
            print "\nYour available letters are: " + str(remaining_letters)
            print "Tries so far " + str(1 + TRIES) + "\n"
            # keeps the number of attempts
            TRIES += 1

            if TRIES == MAX_TRIES - 1:
                guess_word = raw_input("Do you know the word? Type it in here ")
                if guess_word == secretWord:
                    print "Congrats! You win!"
                else:
                    print "Sorry! wrong guess!\nThe secret word is  " + str(secretWord)
                    all_HMpics = "\n".join(HMpics[:])
                    print all_HMpics
                    condition = False
                    playAgain()

            # the game finishes when the user has reached the MAX_tries = the length of the word
            elif TRIES == MAX_TRIES:
                print "Sorry! You loose! The Secret Word was: " + str(secretWord)
                # prints all the hangman lines
                all_HMpics = "\n".join(HMpics[:])
                print all_HMpics
                condition = False
                playAgain()

            # the game finishes when the user has guessed the Secret Word
            elif isWordGuessed(secretWord, lettersGuessed):
                print "Congrats! You beat the computer"
                condition = False
                playAgain()

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
