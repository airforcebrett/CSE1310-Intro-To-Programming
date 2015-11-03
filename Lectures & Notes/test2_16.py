def func_list(x,y):
    i=0
    j=0
    new_list=[]
    k=abs(len(x)-len(y))
    if len(x)>=len(y):
 
        while i<len(y):
            new_list.append(x[i]+y[i])
            i=i+1
        while j<k:
            new_list.append(x[i])
            j=j+1
        return(new_list)
    else:
        
        while i<len(x):
            new_list.append(x[i]+y[i])
            i=i+1
        while j<k:
            new_list.append(y[i])
            j=j+1
        return(new_list)
def main():
    x=[1,2,3,4]
    y=[10,20,30,40,50]
    print("New List: ", func_list(x,y))

main()
