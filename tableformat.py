"""Print a table with powers of 10 from 0 to N (N = 10).
Format the whole row at once. User choose the width for dispalying the data."""

N = 10
w_i = int(input("Enter the width to display i: "))
w_pow = int(input("Enter the width to display 10**i: "))


h_line = '--------------------'

print(h_line)
# should produce: "| %3s | %13s |"
format_str = "| %" + str(w_i) + "s | %" + str(w_pow) +"s |"
# want: "| %3s | %13s |" % ('i', '10**i')
header_str = format_str % ('i', '10**i')
print(header_str)
print(h_line)
i = 0
while i <= N:
    # should produce: "| %3i | %13i |"
    format_str = "| %" + str(w_i) + "d | %" + str(w_pow) +"i |"
    row_str = format_str % (i, 10**i)
    print(row_str)

    i = i + 1

print(h_line)

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
