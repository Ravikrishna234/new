"""HAND"""
def calculateHandlen(hand):
    """hand"""
    sum = 0
    for i in hand:
    	sum = sum + hand[i]
    return sum
    

def main():
	"""hand"""
	n=input()
	adict={}
	for i in range(int(n)):
		data=input()
		l=data.split()
		adict[l[0]]=int(l[1])
	print(calculateHandlen(adict))
		


if __name__== "__main__":
	main()