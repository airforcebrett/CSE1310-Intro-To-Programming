def my_count(L,N):
    print("\t First line of my_count: L= ",L, "N= ",N)
    c=0
    i=0
    while i<len(L):
        if L[i]==N:
            c=c+1
        i=i+1
    
    print("\t last line before return of my_count")
    return c
    

#main code
print("first line of the main code")
L=[7,1,2,0,9,2,2]
X=2
count=my_count(L,X)
print("They are ",count, "occurences of ",X, " in ", L)
count=my_count([4,1,2],8)
print("They are ",count, "occurences of ",X, " in ", L)

print("last line of the main code")


