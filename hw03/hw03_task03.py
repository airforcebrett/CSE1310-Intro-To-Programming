"""
Brett Bishop
1000425627
9/15/14
Task 3 for homework 3 is a program that repeatedly asks the user to enter two real numbers. It
stops when the numbers entered by the user are equal. It will count how many pairs were entered
and computes the distance between them.
"""
import math

i=0
k=0
dist_var2=1000
while i<1:
    n1=int(input("Enter number 1: "))
    n2=int(input("Enter number 2: "))
    dist_var=math.fabs(n1-n2)
    if n1==n2:
        break
    else :
        k=k+1
        if dist_var<dist_var2:
            dist_var2=dist_var
        
if dist_var2==1000:
    dist_var2=float(0.0)
     
        
    
        


print("You entered : ",k," pairs")
print("The minimum distance is : ", dist_var2)
