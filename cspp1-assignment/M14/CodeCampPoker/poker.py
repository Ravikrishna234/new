"""CAMPPOKER"""
def is_straight(hand):
    """POKER"""
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])    
    face_values.sort()
    for i in range(0, len(face_values)-1):
        if face_values[i+1]- face_values[i] != 1:
            return False
    return True
def is_flush(hand):
    """POKER"""
    suit = hand[0]
    for h_input in hand:
        if suit[1] != h_input[1]:
            return False
    return True
def four_of_a_kind(hand):
    """POKER"""
    for i in range(len(hand)):
        suit = hand[i]
        count = 0
        for h_input in hand:
            if suit[0] == h_input[0]:
                count += 1
        if count == 4:
            return True
    return False
def full_house(hand):
    """POKER"""
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])
    face_values.sort()
    face = set(face_values)
    if len(face) == 2:
        return True
    return False
def Three_of_akind(hand):
    """POKER"""
    for i in range(len(hand)):
        suit = hand[i]
        count = 0
        for h_input in hand:
            if suit[0] == h_input[0]:
                count += 1
        if count == 3:
            return True
    return False
def Two_pair(hand):
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])
    face_values.sort()
    face = set(face_values)
    if len(face) == 3:
        return True
    return False
def one_pair(hand):
    """POKER"""  
    card_values = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14, '2':2, '3':3,
                    '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    face_values = []
    for h_in in hand:
        face_values.append(card_values[h_in[0]])
    face_values.sort()
    face = set(face_values)
    if len(face) == 4:
        return True
    return False
def hand_rank(hand):
    """POKER"""
    if is_straight(hand) and is_flush(hand):
        return 8
    elif four_of_a_kind(hand):
        return 7 
    elif full_house(hand):
        return 6       
    elif is_flush(hand):
        return 5
    elif is_straight(hand):
        return 4
    elif Three_of_akind(hand):
        return 3
    elif Two_pair(hand):
        return 2
    elif one_pair(hand):
        return 1               
    else:
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
