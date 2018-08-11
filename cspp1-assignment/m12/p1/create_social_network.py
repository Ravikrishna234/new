"""SOCIALNETWORK"""
def create_social_network(data):
    """social"""
    return data

def main():
    """social"""
    dictionary_ = {}
    lines_ = input()
    i = ''
    for i in range(int(lines_)):
        string_ = input()
        index_ = string_.split()
        if index_[0] not in dictionary_:
            dictionary_[index_[0]] = [index_[2]]
        else:
            dictionary_[index_[0]].append(index_[2])
    print(create_social_network(dictionary_))

if __name__ == "__main__":
    main()
