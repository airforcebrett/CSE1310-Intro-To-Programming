def read_file(fnm):
    fp=open(fnm,'r')
    t=[]
    for line in fp:
        line=line.strip().split(',')
        t.append(line)

    print(t)


def main():
    x="vet.txt"
    read_file(x)
        
        
        

main()
        
