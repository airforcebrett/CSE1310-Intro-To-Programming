def double(x,y):
    x=2*y
    print('double: ',x,y)
    return x
def main():
    m=4
    while m>1:
        k=m%3
        print("main:",double(m,k))
        print("main:m=",m)
        m=m-1

main()
