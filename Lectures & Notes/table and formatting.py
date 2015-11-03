"""
print a table with powers of 10 from 0 to N n =10
"""

N=10
h_line='------------------------------------'
w_i=int(input("Enter the width i:"))

w_pow=int(input("Enter the width: "))
          
print(h_line)
print('| i |   10**i    |')
print(h_line)
i=0

while i<=N:
   # i_str="%3i"%(i)
#    pow_str="%-13i"%(10 ** i)
 
    format_str= " | %"+str(w_i)+"d | %"+str(w_pow)+"i |"
    row_str=format_str % (i, 10**i)
    print(row_str)
    i=i+12
    
print(h_line)
