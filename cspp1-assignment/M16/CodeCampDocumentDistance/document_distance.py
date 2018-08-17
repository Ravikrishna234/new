"""DOCUMENTDISTANCE"""
filename="stopwords.txt"
import math
def similarity(dict1, dict2):
    """DISTANCE"""
    l=''
    for i in dict1:
        for j in i:
            if j not in '~!@#$%^&*()_+=?1234567890':
                l = l + j
    s=''
    for i in dict2:
        for j in i:
            if j not in '-~!@#$%^&*()_+=?1234567890':
                s = s + j

    lis1=l.split()
    lis2=s.split()
    lis3 = lis1 + lis2
    dict3={}
    for word in lis3:
        if word not in load_stopwords(filename).keys():
            dict3[word] = (lis1.count(word),lis2.count(word))
    print(dict3)
    numerator = 0
    denominator = 0
    for i in dict3:
        numerator = numerator + (dict3[i][0] * dict3[i][1])
        denominator = denominator + (math.sqrt(dict3[i][0]**2)) * (math.sqrt(dict3[i][0]**2))
    similarity1 = (numerator / denominator)
    return similarity1
def load_stopwords(filename):
    """DISTABCE"""
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    """DISTANCE"""
    input1 = input().lower()
    input2 = input().lower()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
