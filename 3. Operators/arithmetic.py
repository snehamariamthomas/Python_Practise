""" 
ARITHMETIC OPERATOR
+ 
- 
/ : ALWAYS IN FLOAT
* 
**: POWER

//: LOWER DIVISION - gives dividend/ ALWAYS INT / 
gives lower value in case of NEGATIVE

%: MODULUS OPERATOR - gives remainder | incase dividend is less than divisor then gives dividend. 
ex: 5 % 8 --> 5
"""

A = 2**8
print(A)

a = -15
b = 7
print(a / b)  # -2.142857142857143
print(a // b)  # -3 : lower value i.e. -2 or -3 so lower is -3

a = -15
b = 7
print(a % b)

""" 
-15/7= -2.14 which will be floored tp -3
-15 = quotiesnt* divisor + remainder
-15 = (-3*7)+6
so answer is 6
"""

""" 
16%5
-16/5 = -3.2 --- -4
-16= (-4*5)+4
remainder= 4 
"""
