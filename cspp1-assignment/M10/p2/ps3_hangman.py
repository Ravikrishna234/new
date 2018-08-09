"""HANGMAN"""
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """hangman"""
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
    """hang"""
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """hang"""
    co_unt = 0
    len_gth = len(secret_word)
    for i in secret_word:
        if i in letters_guessed:
            co_unt += 1
    if co_unt == len_gth:
        return True
    return False
def getGuessedWord(secretWord, lettersGuessed):
    """hang"""
    count = 0
    blank = ['_'] * len(secretWord)
    st_r = ''
    for i in secretWord:
        if i in lettersGuessed:
            st_r = st_r + i
        else:
            st_r = st_r + '_'
    return st_r
def getAvailableLetters(lettersGuessed):
    """hang"""
    import string
    st_r = ''
    count = dict((key, 0) for key in string.ascii_lowercase)
    for char in count.keys():
        if char not in lettersGuessed:
            st_r = st_r + char
    return st_r
def hangman(secretWord):
    """hang"""
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    totalchances = 8
    wordguessed = False
    print("Welcome to the game,Hangman")
    print("I am thinking of a word that"+intro+"letters long")
    print("-------------")
    while totalchances>0 and totalchances <= 8 and wordguessed is False:
        if secretWord == getGuessedWord(secretWord,lettersGuessed):
            wordguessed = True
            break
        print("You have"+str(totalchances)+"guesses left")
        print("Available letters" + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a word").lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print("Oops ! you have already guessed that letter" + getGuessedWord(secretWord, lettersGuessed))
                print("-------")
            else:
                lettersGuessed.append(guess)
                print("Good guess" + getGuessedWord(secretWord,lettersGuessed))
                print("-------")
        else:
            if guess in lettersGuessed:
                print("Oops ! you have already guessed that letter" + getGuessedWord(secretWord,lettersGuessed))
                print("-------")
            else:
                lettersGuessed.append(guess)
                totalchances = -1
                print("Oops! that letter is not my word" + getGuessedWord(secretWord,lettersGuessed))
    if wordguessed == True:
        return "congratulations,you won"
    elif totalchances == 0:
        print("Sorry, you ran out of Guesses.The word"+ str(secretWord))
def main():
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
if __name__ == "__main__":
    main()