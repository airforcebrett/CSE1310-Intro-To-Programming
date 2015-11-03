"""
Brett Bishop
1000425627
9/10/14
Task 1,2 & 3 problems for homework 2
"""


"""
For each task below, put your answers in this file. Follow the conventions:
T - for True
F - for False
NONE - for no value
ANY - for every possible value

IMPORTANT NOTE:
This file will be graded by a program. You must follow the conventions or else
it will be graded as being wrong because it will not math what the program is looking for).
"""


"""
Task 1  (5 points)
Fill out the answer: T (for True) or F (for False). If the expression is not fully
parenthesized, use parenthesis to show the order of operators being evaluated.
Example:
A, B, C :
F, F, T   : (A==B) or C    : T
"""

A, B, C   :  expression               : evauates to (T/F)
T, T, T   : ((A and (not B)) and C )    : F
T, F, T   : ((not A) or (B or (not C))) : F
F, T, T   : ((A or B) and (B or C))     : T
5, 0, 'F' : ((A >= B) and bool(C) )    : T
8, 9, 2   : ((A % B) > (B % C) )        : T

"""
Task 2 (5 points)
Give boolean values to A, B, and C that make the following boolean expressions
evaluate to True (T) and to False (F). E.g. for

(A and (not B)) and C
 :  A, B, C
T:
F:

on the line:
T:
list the values for A, B and C (in this order and separated by commas) that make
the expression evaluate to True.
"""
 
(A and (not B)) and C
 :  A, B, C
T: T,F,T
F:T,T,T

(3 > A) and (3 < A)
     A
T: NONE
F:  5


(3 >= A) or (3 < A)
     A
T: 3
F: NONE

(3 >= A) or (10 < A)
     A
T: 2
F: 10
    

"""
Task 3  (10 points)
Each of the lines below gives values for a,b,c,d. For each line,
your answer will be every number, x, between a and b (a <= x <= b),
for which the remainder when dividing x by c is d.
Write your answers below as show in the example line (the first line).
** If you think there are no such numbers (if you can not think of any number
that has these properties say: NONE  (see example in teh second line).
Note: 7 and 9 are part of the answer in the example in the first row
because they are between 7 and 14 and 7%2 is 1 and 9%2 is 1.

Example:
 a,  b , c , d : your answer
 7,  14,  2, 1 : 7, 9, 11, 13 
14,  7 ,  2, 1 : NONE   #  (there are no numbers x s.t.: 14<=x<=7)

"""
 a,  b , c , d : your answer
 1, 100, 20, 0 : 20,40,60,80,100
 1, 100, 10, 6 : 6,16,26,36,46,56,66,76,86,96
 1, 100, 10, 10: NONE #( there are no numbers x s.t.: x%10=10)
17,  62, 17, 5 : 22,39,56
17,  62, 62, 0 : 62        

