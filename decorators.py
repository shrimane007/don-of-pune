# def decor1(func):
#     def inner():
#         x=func()
#         return x*x
#     return inner 
# def decor (fun):
#     def inner():
#         x=fun()
#         return 2*x
#     return inner    
# @decor1
# @decor
# def num():
#     return 10
# print(num())

# def hard(func):
#     def inner():
#         a=func()
#         mult=5*a
#         return mult
#     return inner
# def decor(fun):
#     def inner():
#         c=fun()
#         add=c+5
#         return add
#     return inner
# @decor
# @hard
# def job():
#     return 1000
# print(job())

# def decor(func):
#     def inner(nam):
#         if nam=="sunny":
#             print("hey sunny")
#         else:
#             func(nam)
#     return inner
# @decor

# def wish(name):
#     print("hello",name,"hii")
# wish("durga")
# wish("sunny")

# def decor(func):
#     def inner(nam):
#         print("hii")
#         func(nam)
#     return inner
# @decor

# def wish(name):
#     print("hello",name,"hii")
# wish("durga")
# wish("sunny")

# def decor(func):
#     def inner(nam):
#         if nam=="sunny":
#             print("hey sunny")
#         else:
#             func(nam)
#     return inner
# @decor

# def wish(name):
#     print("hello",name,"hii")
# wish("durga")
# wish("sunny")
 
# def hard(func):
#     def inner(f):
#         print("hey shri 1")
#         func(f)
#     return inner
# def decor(fun):
#     def inner(a):
#        print("hey shri 2")
#        fun(a)
#     return inner
# def decorx(funy):
#     def inner(l):
#         print("hey shri 3")
#         funy(l)
#     return inner
# @hard
# @decorx
# @decor
# def job(w):
#     print("hey shri",w)
# job(0)
