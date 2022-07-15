# def sum_min(a,b):
#     sum=a+b
#     mn=a-b
#     return sum ,mn
# x,y=sum_min(10,20)
# print(x)
# print(y)

# def calc(a,b):
#     sum=a+b
#     min=a-b
#     mult=a*b
#     div=a/b
#     return sum,min,mult,div
# t=calc(100,50)
# print(t)

# def wish(name="guest"):
#     print("Hello",name,"gm")
# wish("shri")
# wish()

# def f1(*n):
#     total=0
#     for x in n:
#         total=total+x
#     print(total)
# f1()
# f1(10,20)
# f1(10,20,30)

# def f(**n):
#     for k,v in n.items():
#         print(k,"=",v)
# f(g=10,h=20)
# f(shri="namme",dhiru=20)

# a=10
# def f1():
#     # global a
#     a=222
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

## recursive fun=
 
# def fact(n):
#     if n==0:
#        result=1
#     else:
#         result=n*fact(n-1)
#     return result
# print(fact(5))


#  lambda arg:expression

# s=lambda n:n*n
# print(s(4))

# s=lambda x,y:x+y
# print(s(10,20))

# s=lambda x,y:x if x>y else y
# print(s(80,50))

## filter(function,sequence)
# def iseven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# i=[55,68,65,35,655,6,]
# l=list(filter(iseven,i))
# print(l)

# i=[10,55,5,6,335,2,55]
# l=list(map(lambda x:x if x%2==0 else False, i))
# print(l)

# i=[10,55,5,6,335,2,55]
# l=list(filter(lambda x:x if x%2==0 else False, i))
# print(l)

## map(func,seq)=

# i=[10,52,520,560,65,656,6562,932]
# def f1(x):
#     return 2*x
# l1=list(map(f1,i))
# print(l1)

# i=[10,52,520,560,65,656,6562,932]
# l=list(map(lambda x:x*2 ,i))
# print(l)

# s=[1,2,3,4,5,6,7]
# l=[8,9,10,20,30,40]
# k=list(map(lambda x,y:x*y ,s,l))
# print(k)

# a=[0,1,1,2,3,5,8]
# b=lambda x,y:x+y+y
# print(b(0,1))
# s=[1,2,3,4,5,6]
# a=list(map(lambda x:x*x,s))
# print(a)

# from functools import *
# s=[0,1,1,2,3,5,8]
# s1=reduce(lambda x,y:x+y,s)
# print(s1)

# def f1():
#     def inner (a,b):
#         print("sum",a+b)
#         print("mult",a*b)
#     inner(10,20)
    
# s=f1()
# print(s)


# def outer():
#     print("its outer")
#     def inner(a,b):
#         print("sum=",a+b)
#         return a+b
#     return inner
# s=outer()
# s(10,20) 

### DECORATOR= without modifing original functional it added some functionality
## get code shorter 

# def decor(func):
#     def inner(name):
#         if name=="durga":
#             print("hello bad m")
#         else:
#             func(name)
#     return inner
# @decor        ## link wish to dec function
# def wish(nam):
#     print("Hello",nam,"Gm")
# wish("shri")
# wish("akki")
# wish("durga")

# def decor(func):
#     def inner(name):
#         if name=="durga":
#             print("hello bad m")
#         else:
#             func(name)
#     return inner
        
# def wish(nam):
#     print("Hello",nam,"Gm")
# wish("durg")
# wish("durga")
# decorfunction=decor(wish)      ## link wish to dec function


# wish("shri")
# wish("akki")
# wish("durga")
# wish("kk")
# decorfunction("durga")
# decorfunction("shri")

# def smart(func):
#     def inner(a,b):
#         if b==0:
#             print("unable to print")
#         else:
#             return func(a,b)
#     return inner

# @smart

# def div(a,b):
#     return a/b
# print(div(10,5))
# print(div(10,0))













































