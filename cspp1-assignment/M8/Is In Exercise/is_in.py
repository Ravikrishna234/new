"""Is in character"""
def isIn(char, aStr):
    """char"""
    length = len(aStr)
    middle = length // 2
    if length == 0:
        return False
    if length == 1:
        if char == aStr:
            return True
        else:
            return False
    if aStr[middle] == char:
        return True
    elif aStr[middle] > char:
        return isIn(char,aStr[0:middle])
    elif aStr[middle] < char:
        return isIn(char,aStr[middle:length+1])


def main():
    """char"""
    data = input()
    data = data.split()
    print(isIn((data[0][0]),data[1]))


if __name__ == "__main__":
    main()
