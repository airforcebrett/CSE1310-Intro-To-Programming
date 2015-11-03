"""
Brett Bishop
1000425627
9/10/14
Task 6 for homework 2 is a program that takes two integers a and b and will compute a/b
and b/a. Cannot divide by zero so it will print INF otherwise print the result of the division.

"""

a=int(input("Enter a: "))
b=int(input("Enter b: "))


if a==0:
    if b==0:
        print("INF")
        print("INF")

    else:
        print(float(a/b))
        print("INF")
else :
    if b==0:
        print("INF")
        print(float(b/a))
    else:
        print(a/b)
        print(b/a)
    
    
