
def main():
    d={10 : "Once",
       20: "upon",
       30: "a",
       40: "time",
       50: ", "}
    print(d)
    L=list(d.keys())
    print(L)
    i=0
    while i<len(L):
        k=L[i]
        if len(d[k])<3:
            d[d[k]]="There was a king"
        i+=1
    print(d)
    for k in d:
        print(k,d[k])

main()
