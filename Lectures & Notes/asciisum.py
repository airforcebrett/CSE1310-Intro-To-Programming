""" Write a fct named ascii_sum that will return the sum of
all ascii numbers in the string"""

def ascii_sum(x):
   
    if type(x) is not str:
        return ('-1')
    else:
        i=0
        my_sum=0

        while i< len(x):
            my_sum=my_sum+ord(x[i])
            i=i+1
            return(my_sum)



def main():
    i=0
    x=input("Enter a string: ")
    my_sum=ascii_sum(x)
       
        
    print(my_sum)
    

main()
