def foo(n):
    i=1
    while i<=100:
        if i%n==0:
            print(i)
            i=i+1
        else:
            i+=1
        
  
def main():
    n=10
    foo(n)

main()
