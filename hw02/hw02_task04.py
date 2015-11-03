"""

9/10/14
Task 4 for homework 2 is a program that asks the user to enter two integers,n and d and
if divisible n by d it will print the integer and the remainder part of the division.

"""

n=int(input("Enter n: "))
d=int(input("Enter d: "))

div_var=int((n / d))
rem_var=(n%d)

if (n%d==0) :
 
    print(n,' / ', d,' = ',div_var)

else :
    
    print(n,' / ', d,' = ',div_var, '(remainder: ',rem_var,' )')

