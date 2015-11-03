def ftable(N,M):
    i=0
    j=0
    k=0
    im=10
    
    print(" ")
    while j<N:
        while i<M:
            im=im+1
            print(im, end=" ")
            i=i+1
        i=0
        im=im+10-M
        j=j+1
        print("\n", end="")
def main():
    N=int(input("Enter a number N: "))
    M=int(input("Enter a number M: "))
    ftable(N,M)
    

main()


        
    
