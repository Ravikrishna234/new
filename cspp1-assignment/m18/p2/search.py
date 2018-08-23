"""SEARCHINDEX"""
def search(search_index, query):
    """search"""
    query_1 = query.lower()
    query = query_1.split(" ")
    k=set()
    for i in query:
        if i in search_index:
            target = search_index[i]
            for i in target:
                k.add(i[0])
    return k

def process_queries(search_index, queries):
    '''
        function to process the search queries
        iterate through all the queries and call the search function
        print the results returned by search function
    '''
    for word in queries:
        print(search(search_index,word))

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
        
        queries.append(input())

    process_queries(search_index, queries)

if __name__ == '__main__':
    main()
