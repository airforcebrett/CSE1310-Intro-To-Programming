M = [[3,2,7,5], [-1,1,3,7], [2,0,9,1]]
print("M is: ", M)

i = 0
#k = 0
while i < len(M) :
    #print(M[i])
    k = 0
    while k < len(M[i]):
        print(M[i][k], end = " ")
        k = k + 1
    print()
    i = i + 1



col = int(input("Enter a column (to be displayed: "))
# if user enters 0: 3,-1,2
row = 0
while row < len(M):
    print(M[row][col])
    row = row + 1
