## FOR LOOP-
# s="shriyash mane"
# count=0
# for x in s:
#     count+=1
#     print(x)
# print("the total no characters-",count)    

# s=input("enter some string-")
# i=0
# for x in s:
#     print("the characters at-",i,"index is",x)
#     i+=1 

# for x in range(10):
#     print(x)

# 0-20 print odd no-
# range(21)
# if x%2!=0

# for x in range(1,21,2):   ####other mthod for odd no
#     if x%2!=0:
#         print(x)

# 10-1 in descending order-

# for x in range(10,0,-1):
#     print(x)

# list=eval(input("enter some list-"))
# sum=0
# for x in list:
#     sum=sum + x
# print("the sum-",sum)

### while loop-

# x=1
# while x<=10:
#     print(x)
#     x+=1

# the sum of first n no-

# n=int(input("enter no-"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("sum of first no-",n,"number is-",sum)

# ener name until durga-
# name=""
# while name!="durga":
#     name=input("enter name:")
# print("hello drga thanks for confirmation")  
# 
# enter two names-

# name=""
# pwd=""
# while (name!='durga') or (pwd!='python'):
#     name=input("enter name:")
#     pwd=input("enter pwd:")
# print("hello drga thanks for confirmation")  

# infinite loop-
# i=0
# while True:
#    i=i+1
#    print("hello:",i)

## nested loop-
# loop inside another loop
# for i in range(4):
#     for j in range(4):
#         print("i={} and j={}".format(i,j))



##### write progam to display * in right angled triangled form- 
# enter no of rows=3
# *
# **
# ***
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):       ## no of row
#     for j in range(i):   ## no of star ## i no of times j loop will execue.
#         print("*",end=" ")
#     print()                  ## new line

# n=int(input("Enter row number-"))
# for i in range(1,n+1):  ## alays n=n-1
#     for j in range(i):
#         print("*",end=" ")
#     print()

# n=int(input("Enter row number-"))
# for i in range(n):
#     print('*'*n)
    
# n=int(input("Enter row number-"))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
    
# n=int(input("Enter row number-"))
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#     print()

n=int(input("Enter row number-"))
for i in range(1,n+1):
    print('* '*i)














