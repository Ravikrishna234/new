A=input("Enter a string")
COUNT=0
for i in A:
    if A[i] == 'b' and A[i+1] == 'o' and A[i+2] == 'b':
        COUNT = COUNT + 1


print(COUNT)
