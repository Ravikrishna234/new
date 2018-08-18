
"""BUILDSEARCHNDEX"""
FILENAME = "stopwords.txt"
def load_stopwords(filename):
    """build"""
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


def word_list(text):
    """build"""
    print(text)
    list_1 = ''
    for i in text:
        for j in i:
            if j not in "~!@#$%^&*()_+=;,.?-1234567890":
                if j not in "'":
                    list_1 = list_1 + j
    list_1 = list_1.split()
    return list_1


def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    input_1 = word_list(docs)
    adictionary_ = {}
    for word in input_1:
        if word not in load_stopwords(FILENAME):
            adictionary_[word] = (input_1.count(word))
    return adictionary_
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())

    for key in keys:
        print(key)
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = input()
    # iterate through N times and add documents to the list
    for i in range(int(lines)):
        split_ = lines.split()
        documents.append(split_)

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()
