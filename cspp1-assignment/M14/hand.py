"""HAND"""
import random
class Hand(object):
    """initiated"""
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert isinstance(n) == int
        self.hand_size = n
        self.vowels_ = 'aeiou'
        self.consonants_ = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.deal_new_hand()

    def deal_new_hand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        num_vowels = self.hand_size // 3
        for i in range(num_vowels):
            x_letter = self.vowels_[random.randrange(0, len(self.vowels_))]
            self.hand[x_letter] = self.hand.get(x_letter, 0) + 1
        for i in range(num_vowels, self.hand_size):
            x_letter = self.consonants_[random.randrange(0, len(self.consonants_))]
            self.hand[x_letter] = self.hand.get(x_letter, 0) + 1
    def set_dummy_hand(self, hand_string):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(hand_string) == self.hand_size, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(hand_string), self.hand_size)
        self.hand = {}
        for char in hand_string:
            self.hand[char] = self.hand.get(char, 0) + 1
    def calculate_len(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        """
        for i in word:
            if i in self.hand:
                self.hand[i] -= 1
            return False
        return True
MY_HAND = Hand(7)
print(MY_HAND)
print(MY_HAND.calculate_len())

MY_HAND.set_dummy_hand('aazzmsp')
print(MY_HAND)
print(MY_HAND.calculate_len())

print(MY_HAND.update('za'))
print(MY_HAND)
