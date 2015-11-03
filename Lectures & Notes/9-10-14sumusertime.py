""" Ask the user for a number B.
Repeateadly ask (N times) ask the user for an integer and keep track of the sum."""

N = int(input("Enter N (number of numbers that you want added): "))

my_sum=0
i=0
nums_str=0
while i < N :

    user_int=int(input("Enter a number : "))
    my_sum=my_sum+user_int
    print("Intermediary sum: ",my_sum)
    nums_str=nums_str+str(user_int) + ", "
    i = i + 1

print("The sum is : ",my_sum)
print("You have given the following numbers : ",nums_str)

    

print('Bye')
