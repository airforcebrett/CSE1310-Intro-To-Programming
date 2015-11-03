other=2
x=5
t=3
while(t<10) and (t%7!=0):
    t=t+1
    if (t>other) and (other<=3):
        x=other
        other=x
        print("t= ",t+1)
    else:
        t=t+other
    other=other+2
print(t,x,other)
