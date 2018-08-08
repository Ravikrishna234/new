"""SQUARE"""
def apply_to_each(L, f):
    """sq"""
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
def square(a):
    return a**2
def main():
    """sq"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1,square))

if __name__== "__main__":
    main()