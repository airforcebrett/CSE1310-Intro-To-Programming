"""
Brett Bishop
UT ID 1000425627
9/1/14
This program will compute the monthly salary based on the yearly one.
"""


yearly_sal_str = '45000'   # modify this line to fix the bug 
monthly_sal_int = int(yearly_sal_str) / 12
print('For a yearly salary of', yearly_sal_str, 'the monthly salary is:', monthly_sal_int)

# He needed to remove the comma in 45,000 because python does not use commas in integers.
