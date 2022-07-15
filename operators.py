#symbol for certain operation
#1.arithmatic op
#a\\b-floor div op

a = 55.5
b = 25
print(a/b)
print(a//b)
print(a**b)

w='shri'
a='man'
print(a<w)
#comparison based on alphabetical order

a=10
c=50
if(a<c):
    print("a is lesser than c")
else:
    print("a is not greater than c")    

#bitwise
a=10
b=50
print(a&b)

#assignment operators
x=10
x*=20
print(x)

# ternary opertor
# x=first value if (condition)? else second value
# x=(10<20)?30:40
# print(x)
# in python ternery operator not available


x,y=30,60
a=50 if (x<y) else 20
print(a)

x='shri'
y=25
a='pass' if (y > 35) else 'fail' if (y<20) else 'not pass'
print (a)

x=10 if (20>30) else(40) if (50<60) else(70)
print(x)

# identity operators-
# is ,is not
s=[]
# membership operators-
# in ,not in
s=[10,20,30]
print(10 in s)

import math as m
print(m.sin(10))

from math import sin
print(sin(10))

















