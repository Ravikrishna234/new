it=0
while it<5:
    count=0
    for i in "hello, world":
        count+=1
        if it%2 == 0:
            break
    print("Iteration "+str(it)+";count is:"+str(count))
    it=it+1
