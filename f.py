a=10
b=6
while a>b or a%2!=0:
    a=int(input("Enter A: "))
    b=int(input("Enter B: "))
    if a>b:
        print("A is not strictly less than B")
    elif a%2==0:
        print("A is not odd")
        a=10
        b=6
    elif a%2!=0 and a<b:
        break
