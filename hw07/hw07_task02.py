"""
Brett Bishop
1000425627
10/13/14
HW07 Task 02 part a takes a function center_string and takes object, and List and
centers the object based on the list

"""

def center_string(obj,L_format):
    

    if len(L_format)==1:
        l=(L_format[0]-len(str(obj)))
        
        if l%2==0:
            l=int(l/2)
            temp_o=str(obj)
            s=" "*l+temp_o+" "*l
            s=str(s)
            return(s)
        else:
            l=int((l/2)+.5)
            l2=int(l-1)
            temp_o=str(obj)
            s=" "*l+temp_o+" "*l2
            s=str(s)
            return(s)
    else:
        obj=float(obj)
        pre="%."+str(L_format[1])+"f"
        obj=pre%obj
        temp_o=str(obj)
        l=(L_format[0]-len(temp_o))
        if l%2==0:
            l=int(l/2)
            s=" "*l+temp_o+" "*l
            s=str(s)
            return(s)
        else:
            l=int((l/2)+.5)
            l2=int(l-1)
            s=" "*l+temp_o+" "*l2
            s=str(s)
            return(s)

def load_data(fnm):
    i=0
    d={}
    empty_space=0
    try:
        fp=open(fnm,'r')
        t1=[]
        k=0
        count=0
        for line in fp:
            line=line.strip()
            line_i=line
            if line=='':
                empty_space+=1
            else:
                line=line.split(',')
                t1.append(line)
                key_loc=len(t1[k])-1
                key=t1[k][key_loc]
                key=key.split(' ')
                i=0
                c=len(key)
                while i<c:
                    if key[i]=='':
                        key.remove('')
                        c=c-1
                    else:
                        i=i+1
                    
                t1[k].pop()
                i=0
                j=0
                while i<len(t1):
                    while j<len(t1[i]):
                        space_split=t1[i][j].split(' ')
                        k2=0
                        c=len(space_split)
                        while k2<c:
                            if space_split[k2]=='':
                                space_split.remove('')
                                c=c-1
                            else:
                                k2=k2+1
                        t1[i][j]=space_split[0]
                        j=j+1
                    j=0
                    i=i+1
                try:
                    d[key[0]].append(t1[k])
                    k=k+1
                except KeyError:
                    d[key[0]]=[t1[k]]
                    k=k+1
        for line in d:
            error=len(d[line][0])
            i=1
            while i<len(d[line]):
                if error!=len(d[line][i]):
                    error_found=d[line][i]
                    error_found.append(line)
                    p=0
                    error=''
                    while p<len(error_found):
                        if p+1==len(error_found):
                            error=error+error_found[p]
                            p=p+1
                        else:
                            error=error+error_found[p]+', '
                            p=p+1
                    print("\nERROR! File: ",fnm)
                    print("Found the object with different number of measurements. Line:",error)
                    d={}
                    return(d)
                else:
                    i+=1
        print(d)
        return(d)
        for line in d:
            i=0
            j=1
            k=0
            avg=d[line][i]
            while i<len(avg):
                avg[i]=float(avg[i])
                i+=1
            i=0
            while i<len(d[line][0]):
                while j<(len(d[line])):
                    avg[k]=(avg[k]+float(d[line][j][k]))
                    j=j+1
                j=1
                count=len(d[line])
                avg[k]=avg[k]/count
                prec='%.2f'%avg[k]
                avg[k]=prec
                k=k+1
                i=i+1
            d[line]=avg
            d[line].insert(0,count)
        if empty_space!=0:
            d['']=[1]
        else:
            a=1
        return(d)
    except IOError:
        print("File not found: ",fnm)
        return


def pretty_print(d):
    if len(d)==0:
        d={}
    else:
            
        i=0
        h_line="----------"
        h_len=0
        w_len=0
        for line in sorted(d):
            if len(line)>h_len:
                h_len=len(line)
            else:
                continue
        for line in sorted(d):
            if len(d[line])>w_len:
                w_len=len(d[line])
            else:
                continue
        
        h_len=h_len+4
        h_len1=[h_len]
        h_len2=[8]
    
        print("-"*(h_len-3)+h_line*w_len+"-")
        obj='class'
        print("|"+center_string(obj,h_len1)+"|",end="")
        obj='total'
        print(center_string(obj,h_len2)+"|",end="")
        i=1
        while i<w_len:
            obj='data '+str(i)
            print(center_string(obj,h_len2)+"|",end="")
            i=i+1
        print("\n",end="")
        print("-"*(h_len-3)+h_line*w_len+"-")
        for line in sorted(d):
            obj=d[line][0]
            print("|"+center_string(line,h_len1)+"|",end="")
            print(center_string(obj,h_len2)+"|",end="")
            i=1
            while i<w_len:
                try:
                    obj=d[line][i]
                    print(center_string(obj,h_len2)+"|",end="")
                    i=i+1
                except IndexError:
                    obj='    '
                    print(center_string(obj,h_len2)+"|",end="")
                    i=i+1
                
            print("\n",end="")
    
        print("-"*(h_len-3)+h_line*w_len+"-")
            
def pretty_print2(d):
    for line in d:
        for key in d[line]:
            for this in key:
                print(this)

    

def main():
    fnm="iris.txt"
    d=load_data(fnm)
    pretty_print2(d)
    
    
    
    

main()


