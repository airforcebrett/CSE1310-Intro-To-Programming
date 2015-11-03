def foo1(n):
    print("foo1: ", n)
    res=n*(-1)
    return res
def foo2(n):
    if n>=0:
        print("n is positive")
    else:
        print("n is negative")
    res=foo1(n)
    n=foo1(res)
    print("now n is: ", n)
            
    

def main():
    foo2(5)
main()
