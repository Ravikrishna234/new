"""INCREMENT"""
def apply_to_each(L, f):
    """incr"""
    for i in range(len(L)):
        L[i]=f(L[i])
    return L

def inc(a):
    return a + 1
def main():
    """incr"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1,inc))

if __name__ == "__main__":
    main()
