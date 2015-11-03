def foo(x):
    res=x+10
    print("foo: ", x, res)
    return res
def main():
    i=0
    while i<4:
        foo(foo(i))
        i+=1
main()
    
