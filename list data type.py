# .operating using split-
# s=input("list-")
# l=s.split(':')
# print(l)

## accessing elements from list-
#1-using index,2-using slice opearator

#### list vs immutability-

# i=[10,20,30]
# i[1]=44
# print(i)

## transverse of list-
# list=[1,2,3,4,5,6,7,8,]
# i=0
# while i<len(list):
#     print(list[i])
#     i=i+1

# s=[1,2,3,4]
# for x in s:
#     print(x)

# s=[1,4,5,6,8]
# for x in s:
#     if x%2!=0:
#         print(x)

# list=["s","b","d"]
# x=len(list)
# for i in range(x):
#     print(list[i],"at + index-",i,"at -index-",i-x)

# s=[10,20,30]
# print(s.count(10))

# s=[10,20,30]
# print(s.index(10))

# l=[10,20,30,40,50,60]
# i=int(input("value-"))
# if i in l:
#     print(i,"available at-",l.index(i))

# else:
#     print(i,"not available")

# l=[10,20,30,40,50,60]
# i=int(input("value-"))
# try:
#     print(i,"available at-",l.index(i))

# except ValueError:
#     print(i,"not available")

# n=[]
# n.append("h")
# print(n)
# n=[]
# for x in range(101):
#     if x%10==0:
#         n.append(x)
# print(n)

#### insert-
# l.insert(index,element)
# ## insert never get error regarding position- 
# l=[10,20,30,40,50,60]
# n=l.insert(1,500)
# print(l)

# l1=["shri","dd","dccc"]
# l2=[10,20,30]
# l1.extend(l2)
# print(l1)
# print(l2)

# s=[1,20,30,35,162] 
# print(s.pop())
# print(s.pop(3))
# print(s)

# s=[1,20,30,35,162]
# s.reverse()
# print(s)

# s=[1,20,30,35,162]
# s.sort()
# print(s)

## reverse of alph order by using sort-
# s=[1020,30,40,80,70,962,5525]
# s.sort(reverse=True)
# print(s)

## alias and cloning---> alias=diff variable for same obj       
## clone= duplicate obj created foe diff vribles
## clone = by slice
# x=[10,20,4,50]
# y=x[:]
# y[1]=444
# print(x)
# print(y)
## clone = by copy()
# x=[10,20,4,50]
# y=x.copy()
# y[1]=444
# print(x)
# print(y)
#### nested list-(list in anothr list)- in matrix form-

# x=[[10,20,30],[40,50,60],[70,80,90]]
# print(x)
# print("elements-")
# for r in x:
#     print(r)
# print("marix-")
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(x[i][j],end=' ')
#     print()    

# s=[[10,20,30],[40,50,60],[70,80,90]]
# print(s)
# for a in s:
#     print(a)
# print("matrix-")
# for i in range(len(s)):
#     for l in range(len(s[i])):
#        print(s[i][l],end=' ')
#     print()        

# for i in range(1,11):
#     print(i*i)

# l1=[x*x for x in range(1,11)]
# print(l1)

# l1=[x+x for x in range(1,11)]
# print(l1)

# l1=[x*x for x in range(1,11) if x%2==0]
# print(l1)

# s=[x for x in range(1,11) if x*x]
# print(s)

# s=[2**x for x in range(1,11) ]
# print(s)

# l=['shri','dd','gg','oorkfi']
# l1=[x[0] for x in l]
# print(l1)

# l=['shri','dd','gg','oorkfi']
# l1=[x for x in l if len(x)>2]
# print(l1)

# n1=[10,20,30,40]
# n2=[30,40,50,60]
# n3=[ x for x in n1 if x not in n2]
# print(n3)

# s="the quick brown fox jumps over the lazy dog".split()
# l=[ [x.upper(),len(x)] for x in s]
# print(l)

### slice= s=[begin:end:-1] end should not be -1 or end+1=0 then result is empty
# s=[1,2,3,4,5,6,7,8,9]
# print(s[-2:-3:-2])  # -3+1=-2(so 8)

# a=['a','e','i','o','u']
# s=input("str-")
# w=[]
# for x in s:
#     if x in a:
#         if x not in w:
#             w.append(x)
# print(w)
# print("no of vowel found -",len(w))            

# s=10,
# print(type(s))

# f= [[14, 6], [8, 21], [94, 8], [56, 3]]
# l = []
# for i in range(len(f)):
#     var = f[0]
#     l.append(var)
#     f.remove(var)
#     a=sorted(l)
# print(a)
# # print(sorted(f))






























































































