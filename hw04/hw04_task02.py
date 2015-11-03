"""

10/4/14
Task 2 for homework 4 is a program that counts the frequency of each letter in the string
which is defined as the count of occurences of a letter divided by the total # of letters.
It will print each letter and its frequency in a table .

"""
S = """
Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.  
Now we are engaged in a great civil war, testing whether that nation, or any nation, so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. 
We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, 
have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated 
to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, 
for the people, shall not perish from the earth.
"""
i=0
k=0
total_count=0
L_counts=[]
j=0
lower_case=65
upper_case=97
a=0
while k<26:
    L_counts.append(0)
    k=k+1
while i<len(S):
    if ord(S[i])>64 and ord(S[i])<=90 or ord(S[i])>96 and ord(S[i])<=122:
        total_count=total_count+1
        while j<len(S) and a<26:
            if ord(S[j])==lower_case or ord(S[j])==upper_case:
                L_counts[a]=L_counts[a]+1
                j=j+1
            else:
                j=j+1
        j=0
        a=a+1
        lower_case=lower_case+1
        upper_case=upper_case+1
        i=i+1
    else:
        i=i+1



print("Total count of letters: ",total_count)
i=0
j=0
a=97
L_freq=[]
L_freq3=[]
L_freq4=[]
while i<len(L_counts):
    L_counts[i]=L_counts[i]/total_count
    L_freq3.append(L_counts[i])
    L_freq.append([L_counts[i],chr(a)])
    L_freq4.append([L_counts[i],chr(a)])
    i=i+1
    a=a+1
L_freq.sort()
L_freq3.sort()
L_freq4.sort()
L_freq4.reverse()
L_freq3.reverse()
L_freq.reverse()
print("The top 3 most frequent letters are:  ", end=" ")
a=97
i=0
j=0
L_freq2=[]
while i<len(L_freq):
    L_freq2.append(L_freq[i])
    i=i+1
while j<3:
    if j!=2:
        print(L_freq4[j].pop(), ' , ', end=" ")
        j=j+1
    else:
        print(L_freq4[j].pop())
        j=j+1
i=0
print("-----------------------\n|  letter  |     freq  |\n-----------------------")
while i<len(L_freq):
    print("|       ", L_freq[i].pop()," |  %.4f"%L_freq3[i],"  |")   
    
    i=i+1

print("-----------------------")
    

