import math
import re
stopwords = "stopwords.txt"
def cleanup_words(input1):
	reg = re.compile('[^a-z]')
	input1 = input1.lower()
	input1 = [reg.sub('',w.strip())for w in input1.split(' ')]
	return input1

def remove_stopwords(input1,input2):
	d={}
	d=load_stopwords(stopwords)
	word_list1=cleanup_words(input1)
	word_list2=cleanup_words(input2)
	word_list=word_list1+word_list2
	dictionary={}
	for word in word_list:
		if word not in d and len(word)>0:
			dictionary[word] = (word_list1.count(word), word_list2.count(word))
	return dictionary
def similarity(d1,d2):
	dictionary = {}
	dictionary = remove_stopwords(d1,d2)
	num = 0
	d1 = 0
	d2 = 0	
	for d in dictionary.values():
		num = num + d[0] * d[1]
		d1 = d1 + (d[0]**2)
		d2 = d2 + (d[1]**2)
	den = math.sqrt(d1) * math.sqrt(d2)
	return(num/den)
def load_stopwords(filename):
	stopwords = {}
	with open(filename,'r') as filename:
		for line in filename:
			stopwords[line.strip()] = 0
	return stopwords
def main():
	input1 = input().lower()
	input2 = input().lower()
	print(similarity(input1, input2))
if __name__ == "__main__":
	main()
