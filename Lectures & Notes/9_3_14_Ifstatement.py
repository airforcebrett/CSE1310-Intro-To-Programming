#9/3/14  If & else statements

score= int(input("Enter a Score: "))
if 0<=score<=100 :
    print(" Here we are on the true branch")
    print(" The Score is valid")
#nested statement below
    if score >=70:
        print("Enjoy 1320")
    else:
        print("Sorry repeat class you failed")
        
else:
    
    print("The score is not valid.")
    print("Here we are on the false branch")
    score=0

    
print("Now the score is:", score)
print('bye')


 #if-elif-else


if 100>=score>=90 : 
           print("A")
elif score>=80:
           print("B")          
elif score>=70:
           print("C")
elif score>=60:
           print("D")
else:
           print("F")
           



