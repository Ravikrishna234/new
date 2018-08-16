"""CAMPPOKER"""
def is_straight(hand):
    """POKER"""
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for face_ in hand:
        face_values.append(card_values[face_[0]])
    face_values.sort()
    for i in range(0, len(face_values)-1):
        if face_values[i+1] - face_values[i] != 1:
            return False
    return True
def is_flush(hand):
    """POKER"""
    suit = hand[0]
    for face_ in hand:
        if suit[1] != face_[1]:
            return False
    return True


def hand_rank(hand):
    """POKER"""
    if is_straight(hand) and is_flush(hand):
        return 3
    elif is_flush(hand):
        return 2
    elif is_straight(hand):
        return 1
    return 0

def poker(hands):
    """POKER"""
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
