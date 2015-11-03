"""
\
10/13/14
HW07 Task 01 that uses a function count() to find how many unique keywords
occur and create another file that contains the lines from the original file but in
decreasing order.

"""

def count(fnm,L):
    i=0
    d={}
    
    try:
        fp=open(fnm,'r')
        t1=[]
        fp2=fnm.split('.')
        fp2[0]=fp2[0]+"_copy"
        fp2[1]="."+fp2[1]
        file=fp2[0]+fp2[1]
        k=0
        for line in fp:
            line=line.strip()
            line_i=line
            line=line.split(' ')
            t1.append(line)
            i=0
            j=0
            p=0
            r=1
            while p<len(t1[k])-1:
                if t1[k][0]==t1[k][r]:
                    t1[k].pop(r)
                    p=p+1
                    r=r+1
                else:
                    p=p+1
                    r=r+1
            count=0
            while i<len(L):
                while j<len(t1[k]):
                    if t1[k][j]==L[i]:
                        count=count+1
                        j=j+1
                    else:
                        j=j+1
                j=0
                i=i+1
            try:
                d[count].append(line_i)
                k=k+1

            except KeyError:
                d[count]=[line_i]
                k=k+1   
        fp_new=open(file,'w+')
        for key in reversed(sorted(d)):
            if len(d[key])>1:
                i=0
                j=0
                while i<len(d[key]):
                    
                    write=str(key)+": "+str(d[key][i])
                    fp_new.write(write)
                    fp_new.write("\n")

                    i=i+1
                    
            else:
                write=str(key)+": "+str(d[key][0])
                fp_new.write(write)
                fp_new.write("\n")
        fp_new.close()

    
    except IOError:
        print("File not found: ", fnm)
    

        

def main():
    fnm=input("Enter a Filename: ")
    L=['CSE','1310','1104','1105']
    count(fnm,L)


main()
    
    
