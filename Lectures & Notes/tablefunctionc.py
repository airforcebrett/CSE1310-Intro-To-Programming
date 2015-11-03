"""table function part c where N rows and M columns"""

def ftable(N,M):
    i=0
    j=0
    k=0
    im=1
    
    print(" ")
    while j<N:
        while i<M:
        
            print("%3d "%im, end=" ")
            im=im+N
            i=i+1
            
        i=0
        
        j=j+1
        im=j+1
        print("\n", end="")
def main():
    N=int(input("Enter a number N: "))
    M=int(input("Enter a number M: "))
    ftable(N,M)
    

main()


        
    
