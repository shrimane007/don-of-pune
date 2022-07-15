# x=eval("10+20+30+70")
# print(x)

# x=eval(input("Enter some data:"))
# print(type(x))
# for x1 in x:
#     print(x1)

# eval convert any type of data into that corresponding type from input.

a,b,c=[eval(x) for x in input("enter 3 data types:").split(',')]
print(type(a))
print(type(b))
print(type(c))



