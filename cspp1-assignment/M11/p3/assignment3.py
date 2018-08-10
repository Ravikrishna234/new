"""VALIDWORD"""
def isValidWord(word, hand, wordList):
	"""valid"""
	count = 0
	length = len(word)
	if word in wordList:
		for i in word:
			if i in hand:
				count += 1
	if length == count:
		return True
	return False
	

    


def main():
	"""valid"""
	word=input()
	n=int(input())
	adict={}
	for i in range(n):
		data=input()
		l=data.split()
		adict[l[0]]=int(l[1])
	l2=input().split()
	print(l2)
	print(isValidWord(word,adict,l2))
		


if __name__== "__main__":
	main()