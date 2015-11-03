"""

9/15/14
Task 5 for homework 3 is a program that asks the user to enter two strings. It will
compute and display the number of positions in the strings that have the same
letter and number of letters from string 1 in 2 also.
"""

s1=input("Enter a string: ")
s2=input("Enter a string: ")
i=0
k=0
j=0
l=0
n=0
if len(s1)<=len(s2):
    
    while i<len(s1):
        if s1[i]==s2[i]:
            k=k+1
            i=i+1
        else :
            i=i+1
            continue
    while j<len(s1):
        while l<len(s2):
            if s1[j]==s2[l] and s1[j]!=s2[l-1] :
                l=l+1
                n=n+1
                continue
            else:
                l=l+1
                continue
        j=j+1
        l=0
else:
    while i<len(s2):
        if s1[i]==s2[i]:
            k=k+1
            i=i+1
        else:
            i=i+1
    i=0
    
    while i<len(s1):
        while j<len(s2):
            if s1[i]==s2[j] :
                n=n+1
                j=j+1
            else :
                j=j+1
                continue
        j=0
        i=i+1
    i=0
    j=0
    l=0
    
        
        


    

        
print("Number of positions with the same letter: ",k)
print("Number of letters from S1 that are also in S2: ",n)
