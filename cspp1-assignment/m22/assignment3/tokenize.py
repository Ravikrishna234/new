'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string_):
	"""tokenize"""
	aDict={}
	for i in string_:
		count_ = string_.count(i)
		if i not in aDict:
			aDict[i] = count_
	return aDict
		  

	
            
def main():
	n=int(input())
	for i in range(n):
		str_ = input().split(",")
	print(tokenize(str_))
    

if __name__ == '__main__':
    main()
