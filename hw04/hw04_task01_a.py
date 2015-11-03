"""
Brett Bishop
1000425627
10/4/14
Task 1 part a) for homework 4 is a program that asks the user for size L_size and creates a list, L with real
numbers in it. The numbers are randomly generated starting
at seed 0. 
"""
import random
random.seed(0)
L=[]

L_size=int(input("Enter a size for L: "))
i=0
while i<L_size:
    num=random.random()
    L.append(num)
    i=i+1

print(L)

    
