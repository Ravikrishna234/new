"""SAMPLE"""
def main():
    """sample"""
    n = input()
    aDictio={}
    sum = 0
    for i in range(int(n)):
        data = input()
        l = data.split(" ")
        if l[0] not in aDictio:
            aDictio[l[0]] = [l[1]]
        else:
            aDictio[l[0]].append(l[1])
    print(sample(aDictio))
def sample(hand):
    """sample"""
    return hand

if __name__ == "__main__":
    main()