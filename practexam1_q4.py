t=3
while t<10:
    print(t)
    if t%2==0:
        print("RED")
        if t==6:
            print("VIOLET")
            t=t-1
            break
        else:
            t=5
            print("BLUE")
        continue
    elif t%5==1:
        print("PINK")
    else:
        print("WHITE")
    print("BLACK")
    t=t+1
print("ORANGE",t)
