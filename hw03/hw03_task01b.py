"""

9/15/14
Task 1 for homework 3 is a program that will compute the value of the expression
x/2+x//2
part b) for all the integer values of x between integers A and B given by the user. 
"""

A=int(input("Enter an integer A: "))
B=int(input("Enter an integer B: "))

i=A

while i<=B:
    x=i/2+i//2
    print(i,' /  2  + ',i,' //  2 = ',x)
    i=i+1
