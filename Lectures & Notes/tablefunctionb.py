"""table function part b where you take N must be postitve
and M columns counting up with N rows. """

def ftable(N,M):
    i=0
    j=0
    k=0
    im=0
    
    print(" ")
    while j<N:
        while i<M:
            im=im+1
            print("%3d "%im, end=" ")
            i=i+1
        i=0
        j=j+1
        print("\n", end="")
def main():
    N=int(input("Enter a number N: "))
    M=int(input("Enter a number M: "))
    ftable(N,M)
    

main()


        
    
