"""CAMPPOKER"""
def is_straight(ranks):
    """POKER"""
    return len(set(ranks)) == 5 and (max(ranks) -min(ranks) == 4)
def is_flush(hand):
    """POKER"""
    suit = hand[0]
    for h_input in hand:
        if suit[1] != h_input[1]:
            return False
    return True
def card_rank(hand):
    """POKER"""
    ranks = sorted(['--23456789TJQKA'.index(face) for face, suit in hand], reverse=True)
    return ranks
def kind(ranks, number_):
    """POKER"""
    for face_ in ranks:
        if ranks.count(face_) == number_:
            return face_
    return 0
def two_pair(ranks):
    """POKER"""
    one = kind(ranks, 2)
    two = kind(sorted(ranks), 2)
    if one and two:
        return (one, two)
    return None
def hand_rank(hand):
    """POKER"""
    ranks = card_rank(hand)
    if is_straight(ranks) and is_flush(hand):
        return (8, ranks)
    if kind(ranks, 4):
        return (7, kind(ranks, 4), ranks)
    if kind(ranks, 3) and kind(ranks, 2):
        return (6, kind(ranks, 3), kind(ranks, 2))
    if is_flush(hand):
        return(5, ranks)
    if is_straight(ranks):
        return(4, ranks)
    if kind(ranks, 3):
        return (3, kind(ranks, 3), ranks)
    if two_pair(ranks):
        return(2, two_pair(ranks), ranks)
    if kind(ranks, 2):
        return(1, kind(ranks, 2), ranks)
    return (0, ranks)
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
