"""ODD TUPLES"""  
def oddTuples(aTup):
    """odd"""
    odd=()
    length = len(aTup)
    for t in range(0,length,2):
        odd = odd + (aTup[t],)
    return odd
    

def main():
    """odd"""
    data = input()
    data = data.split()
    aTup=()
    for j in range(len(data)):
        aTup += (str(data[j]),)
    print(oddTuples(aTup))
        

if __name__ == "__main__":
    main()