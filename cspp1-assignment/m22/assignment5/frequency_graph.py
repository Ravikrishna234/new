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
        count_ = '#'*value
        print(str(list_[j]+" - "+str(count_)))
        j = j + 1

def main():
    """sorted"""
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
