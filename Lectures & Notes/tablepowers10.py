"""Print a table with powers of 10 from 0 to N (N = 10).
Format the whole row at once."""

N = 10

h_line = '--------------------'

print(h_line)
print('| i |   10 ** i   | ')
print(h_line)
i = 0
while i <= N:
    #print('|', i, '|' , 10 ** i , '|')

    row_str = "| %3d | %13i |" % (i, 10**i)
    print(row_str)

    i = i + 1

print(h_line)
