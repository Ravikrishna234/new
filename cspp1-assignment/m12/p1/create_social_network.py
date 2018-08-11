"""SOCIALNETWORK"""
def create_social_network(data):
    """social"""
    return data

def main():
    """social"""
    dictionary_ = {}
    lines_ = input()
    k= ''
    for i in range(int(lines_)):
        k = k + i
        string_ = input()
        index_ = string_.split()
        if index_[0] not in dictionary_ and index_[1] == "follows":
            dictionary_[index_[0]] = index_[2].split(",")
        elif index_[1] == "follows":
            dictionary_[index_[0]].append(index_[2].split(","))
    print(create_social_network(dictionary_))

if __name__ == "__main__":
    main()
