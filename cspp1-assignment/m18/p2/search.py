"""SEARCHINDEX"""
def search(search_index, query):
    """search"""
    adictionary_ = {}
    for key in query:
        for index_ in key:
            if index_ in search_index.items():
                adictionary_ = search_index[index_]
                adictionary_ = search_index[index_]
            print(adictionary_)
    return adictionary_

def process_queries(search_index, queries):
    '''
        function to process the search queries
        iterate through all the queries and call the search function
        print the results returned by search function
    '''
    search_ = search(search_index, queries)
    return search_

def main():
    '''
        main function
    '''
    # This line loads the search index
    search_index = eval(input())

    # read the number of search queries
    lines = int(input())
    # read the search queries into a list
    queries = []
    for i in range(lines):
        lower_ = input().lower()
        split_ = lower_.split(" ")
        queries.append(split_)

    process_queries(search_index, queries)

if __name__ == '__main__':
    main()
