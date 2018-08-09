"""VALUES IN DICTIONARY"""
def how_many(aDict):
    """dict"""
    total = 0
    value_list = {}
    for i in aDict:
        value_list = aDict[i]
        count = len(value_list)
        total += count
    return total
def main():
    """dict"""
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1]]
        else:
            aDict[l[0][0]].append(l[1])
        
    print(how_many(aDict))


if __name__== "__main__":
    main()
