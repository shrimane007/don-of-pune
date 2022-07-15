# exception handling=
# exception=error at runtime

# try:
#     print("hello")
#     print(10/0)          # risky code
# except:
#     ZeroDivisionError
#     print("heu")          ## handling code

# try:
#     print("jfgk")
#     print(10/0)     # risky code
                    
# except NameError:
 
#    print("kk")        ## handling code
# # except ValueError:
# #     print("huu")
#    print("jj")
# finally :
#     print("no perticular error")

# import os 
# try:
#     print("hello")
#     # print(10/0)
#     os._exit(0)          # risky code
# except:
#     ZeroDivisionError
#     print("heu")          ## handling code
# finally:
#     print("jj")

# try:
#     print(1)
#     print(FH)
#     print(3)
# except:
#     ValueError
#     print(57)
# finally:
#     print(44)
# print("result")

## nested try except block-
# try:
#     print("i am outer try")
#     try:
#         print("i am inner try")
#         print(10/0)
#     except ZeroDivisionError:
#         print("division error")
#     finally:
#         print("i am inner finnaly")
# except:
#     print("i am outer except")
# finally:
#     print("i am outer finally")

# try:
#     print("i am outer try")
#     # print(10/0)
#     try:
#         print("i am inner try")
#         print(10/0)
#     except FileNotFoundError:
#         print("division error")
#     finally:
#         print("i am inner finnaly")
#     print("hii")
# except ZeroDivisionError:
#     print("i am outer except")
# finally:
#     print("i am outer finally")
# print("hii 2")

# try:
#     print("i am outer try")
#     try:
#         print("i am inner try")
#         print(10/0)
#     except ZeroDivisionError:
#         print("division error")
#     finally:
#         print("i am inner finnaly")
#     print("hii")
# except FileNotFoundError:
#     print("i am outer except")
# finally:
#     print("i am outer finally")
# print("hii 2")

# try:
#     print("hi")
#     print(10/0) 
# except FileNotFoundError:
#     print("jj")
# finally:
#     print("donr")
# print("kk")

# try:
#     print("i am outer try")
#     try:
#         print("i am inner try")
#         # print(10/0)
#     except FileNotFoundError:
#         print("division error")
#     finally:
#         print("i am inner finnaly")
#         # print(10/0)
#     print(10/0)
# except FileNotFoundError:
#     print("i am outer except")
# finally:
#     print("i am outer finally")
# print("hii 2")

# try:
#     print("hi")
#     print(10/0) 
# except FileNotFoundError:   ## NO OF TIMES ALLOWED
#     print("jj")
# else:
#     print("hii else")   # ONLY ONCE ALLOWED 
# finally:
#     print("donr")
# print("kk")

# class TooOldException(Exception):
#     def __init__(self,arg):
#         self.msg=arg
    
# class TooYoungException(Exception):
#     def __init__(self,arg):
#         self.msg=arg

# age=int(input("Age-"))
# if age > 60:
#     raise TooOldException("cant give bride because too old")
# elif age<18:
#     raise TooYoungException("cant marriege under Age")
# else:
#     print("perfectly matched")

 
# s="kgDgn5154kvj"
#separate alphabates and numerics and sort them in ascending order
#first put numbers then alphabets.5154 kgjnkvj # 1455 
# c =''.join(sorted(s))
# print(c)





















