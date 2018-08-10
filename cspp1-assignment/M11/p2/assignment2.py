"""UPDATEHAND"""

def updateHand(hand, word):
    """hand"""
    hands={}
    for i in hand:
        if i in word:
            value = hand[i]
            value -= 1
            hands[i] = value
    return hands
def main():
    """hand"""
    n=input()
    adict={}
    for i in range(int(n)):
        data=input()
        l=data.split()
        adict[l[0]]=int(l[1])
    data1=input()
    print(updateHand(adict,data1))
        


if __name__== "__main__":
    main()