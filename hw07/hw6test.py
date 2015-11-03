
def remove_empty(t):
    t1=[]
    for s in t:
        s=s.strip()
        t1.append(s)
    return(t1)
def load_file(fnm):
    fp=open(fnm,'r')
    d={}
    
   
    for line in fp:
        line=line.strip().split(',')
        empty=remove_empty(line[0:len(line)-1])

    print(empty)
   
        
            

  

def main():
    
    fnm="vet.txt"
    
    load_file(fnm)

main()
