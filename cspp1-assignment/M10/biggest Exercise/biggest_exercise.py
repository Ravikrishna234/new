"""BIGGEST"""

def biggest(aDict):
    """big"""
    print(aDict)
    i = 0
    L = []
    for k in aDict:
        if len(aDict[k]) >= i:
            i =len(aDict[k])
            L = k
    return L


    

def main():
    """big"""
    n = input()
    aDict={}
    for i in range(int(n)):
        s=input()
        l=s.split()
        j = 0
        if l[0][0] not in aDict:
            print(l[2][0])
            aDict[l[0][0]]=[l[2][j]]
        else:
            aDict[l[0][0]].append(l[2][j])
        j = j + 1
        
    print(biggest(aDict))   


if __name__== "__main__":
    main()