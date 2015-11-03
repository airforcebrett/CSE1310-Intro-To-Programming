"""
Brett Bishop
1000425627
9/10/14
Task 7 for homework 2 is a program that performs the following operations: +, -, *, /, **, //, %
(as defined by Python.) The program will first read the first number, then the operation,
and then the second number.

"""

a=int(input("Enter the first number: "))
b=input("Enter the operation: ")
c=int(input("Enter the second number: "))

if b=='+':
    add_var=a+c
    print(a,' + ',c,' = ',add_var)
else:
    if b=='-': 
        sub_var=a-c
        print(a,' - ',c,' = ',sub_var)
    else:
        if b=='*':
            mult_var=a*c
            print(a,' * ',c,' = ',mult_var)
        else:
            if b=='/':
                div_var=a/c
                print(a,' / ',c,' = ',div_var)
            else:
                if b=='**':
                    mult_var2=a**c
                    print(a,' ** ',c,' = ',mult_var2)
                else :
                    if b=='//':
                        div_var2=a//c
                        print(a,' // ',c,' = ',div_var2)
                    else:
                        if b=='%':
                            rem_var=a%c
                            print(a,' % ',c,' = ',rem_var)
                        else:
                            print("This operation is not recognized.")
                            
            



