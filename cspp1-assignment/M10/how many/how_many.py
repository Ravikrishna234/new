"""VALUES IN DICTIONARY"""
def how_many(aDict):
    """dict"""
    print(aDict)
    print(aDict)
    total = 0
    k = ''
    value_list = {}
    for i in aDict:
        value_list = aDict[i]
        count = len(value_list)
        k = k + i

        total += count
    print(len(k))
    return total
def main():
    """dict"""
    n=input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1].split(",")]
        else:
            aDict[l[0][0]].append(l[1])
        
    print(how_many(aDict))


if __name__== "__main__":
    main()
