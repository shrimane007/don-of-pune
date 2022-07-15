# group/UNIT of statement that use repeatedly defined in one unit called function-
# code reusability
# def wish():
#     print('hello')
# wish()
# wish()

# def wish(name,msg):
#     print(name,'hello',msg)
# wish(name="shri",msg="duddu")
# wish(msg="kalya",name="durga")

# def square(x):
#     print("The square of {} is {} .".format(x,x*x))
# square(10)
# square(568)

# def add(a,b):
#     return(a+b)
# result=add(10,20)    
# print("sum is",result) 
# print("sum is",add(10,20))

#whether given no is even or odd=
# def evenodd(n):
#     if n%2==0:
#         print(n, "given no is even")
#     else:
#         print(n,"no is odd")
# evenodd(11)
# evenodd(10)

# find factorial of no=
# def fact(n):
#     result=1
#     while n>=1:
#         result=result*n
#         n=n-1
#     return result
# #print(fact(5))
# for i in range(1,6):
#     print("{} no factorial is {}".format(i,fact(i)))

## returning multiple values from a function=

# s=int(input("enter no : "))

# def fact(s,f=1):

#     for i in range(1,s+1):
#         f = f*i
#     return f


# def work():
#     for i in range(5):
#         s = int(input("enter no : "))
#         ans = fact(s)
#         print(ans)
# try:

#     shri= work
#     rohit = "raj"
#     shri()
#     rohit()
# except Exception:
#     print(" kdi tr srl input de")

# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum ,sub
# x,y = sum_sub(100,50)
# print("sum=",x)
# print("sub=",y)

# def calc(a,b):
#     sum=a+b
#     div=a/b
#     mul=a*b
#     return sum,div,mul
# t=calc(100,50)
# print("results are=")
# for x in t:
#     print(x)

  





























