"""BIGGEST"""

def biggest(aDict):
    """big"""
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
        if l[0][0] not in aDict:
            aDict[l[0][0]]=[l[1][0]]
        else:
            aDict[l[0][0]].append(l[1][0])
        
    print(biggest(aDict))   


if __name__== "__main__":
    main()