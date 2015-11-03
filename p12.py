sum1=0
k=1
while k<=17:
    if k%2==0:
        k=k+3
    if k%5==0:
        k=k+2
        sum1=sum1+k
    else:
        k=k+1
        print(k,sum1)
