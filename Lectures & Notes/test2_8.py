def foo(x):
    if x<=10:
        x=x+10
    else:
        x=x-10
    print("foo: ",x)
def main():
    x=5
    print("x is: ",x)
    foo(x)
    print("now x is :", x)
    foo(x)
    print("finally x is :", x)

main()
