d=[5,2,1,7,3]
print("when start, d= ",d)
j=len(d)-1
i=0
while i<=j:
    if (d[i]>d[j]):
        d=d[j:]+d[:j]
        print("i=", i, "j=", j, "d=", d)
        i+=1
        j=j-i

print("bye")

