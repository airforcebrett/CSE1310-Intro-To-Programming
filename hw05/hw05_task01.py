"""
Brett Bishop
1000425627
10/13/14
HW05 Task 01
"""
import string

def table_from_string(S):
    i=0
    j=0
    nested_list=S.split(';')
    pretty_table=[]
        
    
    while i<len(nested_list):
        nested_list[i]=nested_list[i].split()
        pretty_table.append(0)
        pretty_table[i]=len(nested_list[i])
        i=i+1
    i=0
    while i<len(nested_list):
        while j<len(nested_list[i]):
            nested_list[i][j]=float(nested_list[i][j])
            j=j+1
        j=0
        i=i+1
    i=0
    while i<len(pretty_table):
        if pretty_table[0]!=pretty_table[i]:
            nested_list=[[]]
            break
        else:
            i=i+1
 
    return(nested_list)
                    
def pretty_print(M):
    i=0
    j=0
    f_line="---------"
    h_line="--------"
    print(f_line,end="")
    print(h_line*(len(M[i])+1),"\n|     |",end="")
    while i<len(M[j]):
        print("%8d"%i,end=" |")
        i=i+1
    i=0
    print("\n",end="")
    print(f_line,end="")
    print(h_line*(len(M[i])+1))
    
    while i<len(M):
        
        print("|%4d"%i , end=" |")
        while j<len(M[i]):
        
            print(" %7.2f "%M[i][j], end="|")
            j=j+1
        print("\n",end="") 
        j=0
        i=i+1
    i=0
    print(f_line,end="")
    print(h_line*(len(M[i])+1))

def row_average(M,r_idx):
    i=0
    
    sum1=0
    if r_idx>=len(M):
        avg=-1
        return(avg)
    else:
        total=len(M[r_idx])
        while i<len(M[r_idx]):
            sum1=sum1+M[r_idx][i]
            i=i+1
            avg=(sum1/total)
    return(avg)

def smallest_1(M,c_idx):
    if M==[[]]:
        temp_min=-1
    else:
        i=0
        j=c_idx
        min_list=[]
        if c_idx%2!=0:
            #do this for odd
            while i<len(M):
                min_list.append(M[i][j])
                i=i+1
            i=0
            j=0
            while i<=len(min_list):
                if i==len(min_list):
                    break
                if min_list[i]%2!=0:
                    i=i+1
                    j=j+1
                else:
                    min_list.pop(j)
                
                
                
        else:
            if c_idx%2==0:
            
            #do this for even"""
                while i<len(M):
                    min_list.append(M[i][j])
                    i=i+1
                i=0
                j=0
                while i<=len(min_list):
                    if i==len(min_list):
                        break
                    if min_list[i]%2==0:
                        i=i+1
                        j=j+1
                    else:
                        min_list.pop(j)
            else:
                error=-1
                return(error)
        i=0
        temp_min=0
        if len(min_list)==0:
            temp_min=-1
        else:
            temp_min=min_list[0]
            while i<len(min_list):
                if min_list[i]<temp_min:
                    temp_min=min_list[i]
                    i=i+1
                else:
                    i=i+1
    
    return(temp_min)
def smallest_all(M):
    L_min=[]
    i=0
    #L=table_from_string(M)
    j=len(M[0])
    while i<j:
        L_min.append(smallest_1(M,i))
        i=i+1
            
    return(L_min)

        
def insert_row(M, r_idx):
    if len(M)==0:
        M=M
    else:
    
        if r_idx<=len(M):
            M.insert(r_idx,[0]*len(M[0]))

        else:
            M.append([0]*len(M[0]))

def insert_column_zero(M,c_idx):
    length=len(M)
    if len(M)==0:
        M=M
    else:
        i=0
        while i<length:
            M[i].insert(c_idx,0)
            i=i+1

def insert_column_data_modify(M,c_idx,new_column):
    if len(new_column)==0 or len(M)>len(new_column):
        M=[[]]
        
        return(False)
    else:
        length=len(M)
    if M==[[]]and len(new_column)!=1 or len(new_column)>len(M) :
        
        return(False)
        
    else:
        a=2
    if len(M)==0:
        M=[[]]
        return(False)
    else:
        i=0
        while i<length and M!=[]:
            M[i].insert(c_idx,new_column[i])
            i=i+1
        
    
        return(True)
def insert_column_data_return(M,c_idx,new_column):
    M_copy=M
    M_copy=insert_column_data_modify(M_copy,c_idx,new_column)
    if M_copy==[[]]:
        return(M_copy)
    else:
        if M_copy==True:
            i=0
            M_copy=M
        
            return(M_copy)
        else:
            M_copy=M
            return(M_copy)
        
          
def main():
    M="0.84 0.76 0.42 0.26;0.51 0.40 0.78 0.30"
    M1=[[3, 1, 6, 8], [5, 9, 4, 2], [7, 5, 0, 5]]
    idx=1
    M2=[[]]
    M3=[4.4,3.5]
    L2=table_from_string(M)
    pretty_print(M1)
    row_average(L2,idx)
    smallest_1(L2,idx)
    smallest_all(M1)
    insert_row(M1,idx)
    insert_column_zero(M1,idx)
    insert_column_data_modify(M2,idx,M3)
    insert_column_data_return(M2,idx,M3)   
    
    
main()
