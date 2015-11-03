"""

10/13/14
HW06 Task 01 that loads a file and manipulates a 'table'

"""

def load_file(filename):
    try:
        fp=open(filename,'r')
        t1=[]
    
        for line in fp:
            line=line.strip()
            t1.append(line)
        i=0
        while i<len(t1):
            t1[i]=t1[i].split(',')
            i=i+1
        i=0
        j=0
        while i<len(t1):
            while j<len(t1[i]):
                space_split=t1[i][j].split(' ')
                k=0
                c=len(space_split)
                while k<c:
                    
                    if space_split[k]=='':
                        space_split.remove('')
                        c=c-1
                    else:
                        k=k+1
                t1[i][j]=space_split[0]
                j=j+1
            j=0
            i=i+1
        return(t1)
    
    except IOError:
        print("File not found: ", filename)


def pretty_print(table,w):
    
    t1=table   
    header=t1[0]
    h_line="-"*(w+1)
    
    print(h_line*len(header))
    print("|",end="")
    i=0
    w_i="%"+ str(w)+"s"
    
    while i<len(header):
        row_str=w_i%(header[i])
        print(row_str,end="|")
        i=i+1
    print("\n",end="")
    print(h_line*len(header))
    print("|",end="")
    i=1
    j=0
    
    while i<len(t1):
        while j<len(t1[i]):
            try:
                b=float(t1[i][j])
                if i==len(t1)-1:
                    if '.' not in t1[i][j] and '.' not in t1[i-1][j]:
                        b=int(t1[i][j])
                        row_str=w_i%b
                        print(row_str,end="|")
                        j=j+1
                    else:
                        b_str="%.2f"%b
                        row_str=w_i%b_str
                        print(row_str,end="|")
                        j=j+1
                else:
                    if '.' not in t1[i][j] and '.' not in t1[i+1][j]:
                        b=int(t1[i][j])
                        row_str=w_i%b
                        print(row_str,end="|")
                        j=j+1
                    else:
                        b_str="%.2f"%b
                        row_str=w_i%b_str
                        print(row_str,end="|")
                        j=j+1
            except ValueError:               
                row_str=w_i%(t1[i][j])
                print(row_str,end="|")
                j=j+1
        if i==len(t1)-1:
            break
        else:
            print("\n",end="|")
            j=0
            i=i+1
        
    print("\n")



def sort_multiple(table, L_top):
    t2=[]
    i=0
    j=0
    c=0
    t2=table
    while j<len(L_top):
        k=L_top[j]
        if k==0:
            break
        else:
            while i<len(table):
            
                x=t2[i][k]
                r=k
                while c<k:
                    t2[i][r]=t2[i][r-1]
                    r=r-1
                    c=c+1
                t2[i][j]=x
                c=0
                i=i+1
            i=0
            j=j+1
    header=t2[0]
    t2.pop(0)
    t2.sort()
    t2.insert(0,header)
    
    return(t2)


    
    

    





def main():
    
    table = load_file('bad_name.txt')
    fnm = input("Enter the file name: ")
    table = load_file(fnm)
    pretty_print(table,10)
    L_top = [3,4,0]
    sort_multiple(table, L_top)
    print("\n\nAfter reordering by L_top = ", L_top, "\n\n")
    pretty_print(table, 10)    
    L_top = [2,4]
    sort_multiple(table, L_top)
    print("\n\nAfter reordering by L_top = ", L_top, "\n\n")
    pretty_print(table, 10)
    print('\n')
    pretty_print(table, 6)

main ()
