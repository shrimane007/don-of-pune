# def mygen():
#     yield 'A'    ## not stored in memeory
#     yield 'B'
# g=mygen()
# print(next(g))
# print(next(g))

# def countdown(num):
#     print("started=")
#     while (num>0):
#         yield num
#         num=num-1
# values=countdown(10)
# for x in values:
#     print(x)

# def mygen(num):
#     while num>0:
#         yield num
#         num=num-1
# x=mygen(5)
# for i in x:
#     print(i)

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f>100:
#         break
#     print(f)

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib ():
#     if f>100:
#         break
#     print(f)

# l=[65,78,99,75,4,22,38,23]
# for i in l: 
#     if i %2==0:
#         l.remove(i)
# print(l)

























































































