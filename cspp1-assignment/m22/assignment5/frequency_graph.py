'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    """sorted"""
    list_ = sorted(dictionary.keys())
    j = 0
    for i in list_:
    	value = dictionary[i]
    	c='#'*value
    	print(str(list_[j]+" - "+str(c)))
    	j = j + 1

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
