def addition(x,y):
    res=x+y
    return res
def subtraction(x,y):
    res=x-y
    return res
def multiplication(x,y):
    res=x*y
    return res
def division(x,y):
    res=x/y
    return res
def main():
    n=input("Enter a string: ")
    if '+' in n:
        x=int(n[0])
        y=int(n[2])
        print(x,"+",y,"=",addition(x,y))
    elif '-' in n:
        x=int(n[0])
        y=int(n[2])
        print(x,"-",y,"=",subtraction(x,y))
    elif '*' in n:
        x=int(n[0])
        y=int(n[2])
        print(x,"*",y,"=",multiplication(x,y))
    elif '/' in n:
        x=int(n[0])
        y=int(n[2])
        print(x,"/",y,"=",division(x,y))

main()
        
