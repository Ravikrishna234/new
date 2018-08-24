def yield_():
    a=0
    b=1
    
    while True:
        c=a+b
        yield c
        a=b
        b=c
k=yield_()
for i in k:
    print(i)
