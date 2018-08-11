"""sample"""
def main():
    """sample"""
    st = input()
    print(len(st))
    k = palindrome(st)
    if k == True:
        print("palindrome")
    else:
        print("Not palindrome")
    
def palindrome(s):
    """sample"""
    if len(s) < 1:
        return True
    elif s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False

if __name__ == "__main__":
    main()
