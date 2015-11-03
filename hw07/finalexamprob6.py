def read_file(fnm):
    fp=open(fnm,'r')
    t=[]
    d={}
    for line in fp:
        line=line.strip().split(',')
        t.append(line)
    for line in t:
        i=0
        while i<len(line):
            if ' 'in line[i]:
                t1=line[i].split(' ')
                line[i]=t1[1]
                i=i+1
            else:
                i=i+1
        key=line[1]
        try:
            d[key].append(line[0])
        except KeyError:
            d[key]=[line[0]]
    for line in d:
        if len(d[line])!=1:
            i=0
            highest=int(d[line][0])
            while i<len(d[line])-1:
                highest=highest+int(d[line][i+1])
                i+=1
            
            d[line]=[int(highest)]
        else:
            d[line]=[int(d[line][0])]
    
        
                
                
            

    return(d)


def main():
    x="vet.txt"
    d=read_file(x)
    for line in sorted(d):
        print(line,":",d[line])
    fnm="new_file.txt"
    fp=open(fnm,'w+')
    for line in d:
        write=str(line)+str(d[line])+"\n"
        fp.write(write)

        
    
        
        
        

main()
        
