""" get a string from the user and turn it into an uppercase"""



s1=input("Enter a string: ")
s2=input("Enter a string: ")

i=0
k=0



if len(s1)<=len(s2):
    while i<len(s1):
        if s2.find(s1[i])!=-1 and s2.find(s1[i])!=s2.find(s1[i-1]):
            k=k+1
            i=i+1
            continue
        else:
            i=i+1
            continue
print("Number of letters from S1 in S2 =",k)



