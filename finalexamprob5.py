def foo(x):
    d={}
    for line in x:
        i=x.index(line)
        
        try:
            if i!=len(x)-1:
                d[line].append(x.index(line,i+1))
            else:
                d[line].append(i)
            
        except KeyError:
            d[line]=[i]


    return(d)

def main():
    x="electric"
    print(foo(x))

main()
        
