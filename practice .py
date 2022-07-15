
#ternary operator=
# a=int(input("first no="))
# b=int(input("second no="))
# x=a if a%2==0  else b
# print("even no is- ",x)

# a=[10,20,30]
# c=min(a)
# print(c)
# import math
# r=5
# print(math,"cube of circle=",r**2)

# from sys import argv
# print("no of argv=",len(argv))

# a,b,c=10,50,60
# s=a,b,c
# if a>b and a>c:
#     print("great no- ",a)
# elif b>c:
#     print("great no -",b)
# else:
#     print("great no -",c)
# print(sorted(s))
# print()

# s=['10','20','30']
# t=''.join(s)
# print(t)

# s="i am shrai"
# print(s.split('z'))

# L=[10,20,30,40]
# mult=1
# for x in L:
#     mult=mult * x
# print(mult)

# l=[10,20,30]
# total=0
# s=len(l)
# sum=0
# while sum<s:
#         total=total+l[sum]
#         sum+=1
# print(total)

# s=[10,20,30]
# total=0
# l=len(s)
# i=0                               ##### ????????
# mult=1
# sum=0
# while i<l:
#     total=mult * s[sum]
#     i+=1
# print(total)

# n=int(input("enter no="))
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     print("* "*i)

# n=int(input("enter no="))
# for i in range(1,n+1):
#     print("* "*i)

# i=list("1234")
# i[0]=i[1]=5
# print(i)

# i=[10,20,30,500,40,90]
# for l in i:
#     if l > 400:
#         print("cant affordable ")
#         break
#     print(l)

# s=input("str=")
# i=0
# for x in s:
#     print("char at {} is {} and char at {} is {}".format(i,x,i-len(s),x))
#     i+=1

# s="shriyash"
# n=len(s)
# i=0
# print("forward direction=")
# while i<n:
#     print("char at {} is {} ".format(i,s[i]))
#     i+=1
# print()
# print("backward direction=")
# i=-1
# while i>=-n:
#     for x in s:
#      print("char at {} is {} ".format(i,s[i]))
#      i-=1

# s="shriyas"
# t="su"
# try:
#     a=s.index(t)
# except ValueError:
#     print("not found")
# else:
#     print("got it")

# s="shriyash"
# s1=s.replace("sh","ab")
# print(s1)

# s="an fgj kd iofh ofj , jd , iouf"
# s1=s.split()
# for x in s1:
#     print(x)

# s=("shri" ,"iffh" ,"jfkl" ,"tokh")
# r='-'.join(s)
# print(r)

# s="shriyash ddsl kojjv jidv"
# p=len(s)-1
# target=''
# while p>=0:
#     target=target+s[p]
#     p-=1
# print(target)

# s=input("str=")
# p=s.split()
# g=[]
# i=0
# while i<len(p):
#     g.append(p[i][::-1])
#     i+=1
# output=' '.join(g)
# print(output)

# s="shri"
# r="mane"
# x=''
# i,j=0,0
# while i<len(s) or j<len(r):
#     if i<len(s):
#         x=x+s[i]
#         i+=1
#     if j<len(r):
#         x=x+r[j]
#         j+=1
# print(x)

# s=input("str=")
# d=[]
# for x in s:
#     if x not in d:
#         d.append(x)
# f=''.join(d)
# print(f)         

# s=input("str=")
# d={}
# for x in s:
#     if x in d:
#         d[x]=d[x]+1
#     else:
#         d[x]=1   
# for k,v in d.items():
#     print("{}={}".format(k,v))

# s="shri"
# print(''.join(reversed(s)))
# def fact(num):
#     result=1
#     while num>=1:
#         result=result*num
#         num=num-1
#     return result
# r=fact(5) 
# print(r) 
# for i in range(1,5):
#     print("the fact of ",i,"is ",fact(i))

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

# l=[10,20,30,40]
# i=len(l)
# for x in range(i):
#     print(x,"at index of=",l[x],"negative index of=",x-i)
# print(4 in l)   
# s=[10,20,23,52,523,52585]
# m=[x for x in s if x%2==0]
# print(m)

# s=[10,20,23,52,523,52585]
# g=[10,56,226,62856,565]
# a=[x for x in s if x not in g]
# print(a)

# s="shriyash is clever boy but due to lack of guide line he is not able to perform well".split()
# print(s)
# d=[[x.upper(),len(x)] for x in s]
# print(d)

# s=['a','e','i','o','u']
# w=input("str=")
# k=[]
# for x in w:
#     if x in s:
#         if x not in k:
#             k.append(x) 
# print(k)

# s={10,20,40}
# e=s.add(65)
# print(s)

# s={10,20,30}
# i=[4,5,6]
# s.add(5)
# print(s)

# s={10,20,30,40,50,2,621}
# g={588,45,626,10,20}
# print(s.symmetric_difference(g))  or use (s^g)

# s=input("type set=")
# d=set(s)
# f={'a','e','i','o','u'}
# o=d.intersection(f)
# print(s,o)

# s={100:'durga',145:'shri'}
# # print(s[100])
# d=s.get(100)
# print(d)

# s="mississipi"
# d={}
# for x in s:
#     d[x]=d.get(x,0)+1
# for k,v in d.items():
#     print(k ,"--",v)

# def job(busines):
#     def inner(occupatio):
#         print("i am engi")
#         busines(occupatio)
#     return inner
# @job
# def occupation(jo):
#     print("i am =",jo)
# occupation("doctor")

















