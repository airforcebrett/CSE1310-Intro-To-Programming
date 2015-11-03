"""
Brett Bishop

9/15/14
Task 2 for homework 3 is a program that we map out in excel

"""

V = 0
I = 1
while I < 4:
    print('out')
    K = 10
    while K + I > 8:
        print('in')
        if I % 2 == 0:
            K = K - 2
            V = V + I
        else:
            V += I
            break
        print("line 1:", I, K, V)
    print("line 2:", I, K, V)
    I = I + 1
print('Bye')
