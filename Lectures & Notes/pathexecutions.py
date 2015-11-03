"""
CSE1305
Exercise:
How many execution paths are there for this program? How do you find them?
Give inputs for a,b, and c that cause this progrram to go through each possible path.

"""
a = 30
b = 14
c = 25

if a > c:  #1st IF 
    print('A')
    2*b
    b = 2*b
    if a > b : #2nd IF
        print('B')
        c = a + b
        print('a,b,c: ',a,b,c)
        if b % 5 == 2: #3rd IF
            print('C')
        print('D')
    else:
        print('E')
    print('F')
print('G')

