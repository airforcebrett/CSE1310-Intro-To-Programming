"""

9/15/14
Task 4 for homework 3 is a program that takes 2 integers from user and
will display all numbers, s, such that are both a multiple of small number and divisor of
large number. If large number is first it will display a message and swap their values.
"""

N_small=int(input("Enter the first number: "))
N_big=int(input("Enter the second number: "))
i=N_small-1

if N_small>N_big:
    k=N_big
    N_big=N_small
    N_small=k
    i=N_small-1
    print("The first number should be smaller. Their value will be swapped.")
          
print("The numbers are: ", end=" ")
while i<N_big:
    i=i+1

    if (N_big%i==0) and (i%N_small==0):
        print(i, end=" ")
    else:
        continue
    
print( )   
print('Bye')

    
