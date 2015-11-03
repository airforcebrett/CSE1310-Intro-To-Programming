L=[[3,8,9],[2,7,4],[2,5,6]]
r=0
while r<3:
    c=0
    while c<3:
        if L[r][c]>L[c][r]:
            L[c][r]=L[r][c]+10
        c+=1
    r+=1

r=0
while r<len(L):
    print(L[r])
    r+=1
    
