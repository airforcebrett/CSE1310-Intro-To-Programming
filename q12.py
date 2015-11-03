
str_1=str(input("enter a string: "))

i=0
while i<len(str_1):
    if 'o' in str_1[i]:
        i=i+1
        continue
    elif 'h' in str_1[i]:
        break
    else:
        print(str_1[i], end=" ")
        i=i+1
