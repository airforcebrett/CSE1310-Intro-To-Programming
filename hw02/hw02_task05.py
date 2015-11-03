"""

9/10/14
Task 5 for homework 2 is a program that simulates three coin tosses by generating 3 random
numbers from the set [1,2]. If 1 was generated it corresponds with heads and 2 with tails. The program
will count how many heads and tails were generated.

"""

import time
import random

i=0
heads=0
tails=0
str_head= "head"+"  (  "+ str(1)+ "  )"
str_tail= "tail"+"  (  "+ str(2)+ "  )"
while i<=2:
    a=random.randint(1,2)
    if a==1:
        i=i+1
        heads=heads+1
        print("Tossing..... ", end=" ")
        time.sleep(0.7)
        print(str_head)
         
    else :
        i=i+1
        tails=tails+1
        print("Tossing..... ", end=" ")
        time.sleep(0.7)
        print(str_tail)

print(heads,' heads and ',tails,' tails')
if heads>tails :
    print("Winner: Heads")
else :
    print("Winner: Tails")
    
