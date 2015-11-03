

n=int(input("Enter a number: "))


if n<0:
    print("Negative,", sep=",",end=" ")
else:
    print("Positive,", sep=",",end=" ")
if n%2==0:
    print("Even,", sep=",",end=" ")
else:
    print("Odd,", sep=",",end=" ")
if n%10==0:
    print("Divisible by 10,", sep="-,-",end=" ")
else:
    print("not divisible by 10,", sep="-,-",end=" ")
if n%37==0:
    print("Divisible by 37")
else:
    print("not divisible by 37")
   



