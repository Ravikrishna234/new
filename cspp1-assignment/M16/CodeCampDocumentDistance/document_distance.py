"""DOCUMENTDISTANCE"""
import math
FILENAME = "stopwords.txt"
def similarity(dictionary_1, dictionary_2):
    """DISTANCE"""
    list_1 = ''
    for i in dictionary_1:
        for j in i:
            if j not in '!@#$%^&*()_+-=,.?1234567890':
                if j not in "'":
                    list_1 = list_1 + j
    list_2 = ''
    for i in dictionary_2:
        for j in i:
            if j not in '!@#$%^&*()_+-=",.?1234567890':
                if j not in "'":
                    list_2 = list_2 + j

    list_1 = list_1.split()
    list_2 = list_2.split()
    list_3 = list_1 + list_2
    dictionary3 = {}
    for word in list_3:
        if word not in load_stopwords(FILENAME).keys():
            dictionary3[word] = (list_1.count(word), list_2.count(word))
    numerator = 0
    denominator = 0
    sum1 = 0
    sum2 = 0
    for i in dictionary3:
        numerator = numerator + (dict3[i][0] * dict3[i][1])
        sum1 = sum1 + dictionary3[i][0] ** 2
        sum2 = sum2 + dictionary3[i][1] ** 2
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
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
