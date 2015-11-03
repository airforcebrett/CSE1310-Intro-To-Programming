"""
Brett Bishop
1000425627
10/4/14
Task 1 part b) for homework 4 is a program that asks the user for size L_size
and creates a list, L with real numbers in it. The numbers are randomly generated
starting at seed 0. For each value , v, in the list, L compute a new value, new_v, using the formula:
7+(v/3). These values will be stored in L_new and print a nice table using 3 digit precision,
space the data with '|' and string formating % operator. 
"""
import random
random.seed(0)
L=[]
L_new=[]
L_size=int(input("Enter a size for L: "))
i=0
while i<L_size:
    num=float(random.random())
    L.append(num)
    v=(7+num/3)
    L_new.append(v)
    i=i+1


i=0
k=0
j=0
a=0
print("--------",end="")
while a<len(L):
    print(12*'-',end="")
    a=a+1

print("\n| L        ", end=" ")
while k<L_size:
    print(" | ","%.3f"%L[k], end=" ")
    k=k+1
k=0
print("| \n--------",end="")
while i<len(L):
    print(12*'-',end="")
    i=i+1

print("\n| L_new",end=" ")
while k<L_size:

    print(" | ","%.3f"%L_new[k],end=" ")
    k=k+1
print("|")
print("--------",end="")
while j<len(L):
    print(12*'-',end="")
    j=j+1

    


    
