"'bob'"
A = input("Enter a string")
COUNT = 0
L = len(A)
B = "bob"
for i in range(L):
    if B == A[i:i+3]:
        COUNT = COUNT + 1
print(COUNT)
