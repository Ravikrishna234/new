"""STEPS"""
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """step"""
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """step"""
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
def getWordScore(word, n):
    """step"""
    sum = 0
    for letter in word:
        if letter in SCRABBLE_LETTER_VALUES:
            sum = sum + SCRABBLE_LETTER_VALUES[letter]
    if n == len(word):      
        return sum*len(word) + 50
    return sum*len(word) 
def displayHand(hand):
    """step"""
    string =''
    for letter in hand.keys():
        for j in range(hand[letter]):
            string += letter+' ' 
    return string                             

def dealHand(n):
    """step"""
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand
def updateHand(hand, word):
    """step"""
    new_hand = dict(hand)
    for letter in word:
        if letter in new_hand:
            new_hand[letter]-=1
    return new_hand
            
def isValidWord(word, hand, wordList):
    """step"""
    if word not in wordList:
        return False
    word_dict=getFrequencyDict(word)
    for letter in word_dict:
        if letter not in hand:
            return False
        if word_dict.get(letter)>hand.get(letter):
            return False
        return True
    
def calculateHandlen(hand):
    """step"""
    sum = 0
    for i in hand:
        sum += hand[i]
    return sum

def playHand(hand, wordList, n):
    """step"""
    totalScore = 0
    while calculateHandlen(hand) > 0:
        print('current hand',displayHand(hand))
        data = input("Enter word, or a . to indicate that you are finished:")
        if data == '.':
            print('Goodbye! Total score: '+ str(totalScore)+' points.')
            break
        else:
            if not isValidWord(data,hand,wordList):
                print('Invalid word, please try again.')
            else:
                wordScore = int(getWordScore(data,HAND_SIZE))
                totalScore += wordScore
                print(data +"earned"+str(wordScore)+"points.Total:"+str(totalScore)+" points")
        
                hand = updateHand(hand, data)
    print('Run out of letters.Total score:'+str(totalscore)+'points.') 

def playGame(wordList):

    """set"""
    hand = {}
    while True:
        user_input=input("enter n(new game)|enter r(to play the last hand)|enter e(exit)")
        if user_input == 'n':
            hand = dealHand(HAND_SIZE)
            adict = dict(hand)
            print(adict)
            displayHand(hand)
            playHand(hand,wordList,HAND_SIZE)
        elif user_input == 'r':
            if hand == {}:
                print("You should play a new game then come here")
            else:
                playHand(adict,wordList,HAND_SIZE)
        elif user_input == 'e':
            exit(0)
        else:
            print("Invalid Input")

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    main()
    