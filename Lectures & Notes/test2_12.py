L=[3,7,2,9,1]
count=0
print(count, -1, L)
test=False
while not test:
    count=count+1
    test=True
    i=0
    while i<len(L)-1:
        if (L[i]>L[i+1]):
            temp=L[i+1]
            L[i+1]=L[i]
            L[i]=temp
            test=False
            print(count, i, L)
        i+=1
print("bye")
