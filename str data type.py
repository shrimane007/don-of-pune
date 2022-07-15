# s=input("enter some string-")
# i=0
# for x in s:
#     print("the char.present at +ve index: {} and at -ve index{} is:{} ".format(i,i-len(s),x))
#     i=i+1

# s=[1,2,3,4,5,6,7]
# print(s[-1:-6:-2])


# s=input("entr some sreing:")
# n=len(s)
# i=0
# print("data in forward direction")
# while i<n:
#     print(s[i],end='')
#     i+=1
# print()
# print ("data in backward direction-")
# i=n-1
# while i>=0: 
#     print(s[i],end='')
#     i=i-1
# print()
# print("data in bkwrd-")
# i=-1
# while i>=-n:
#     print(s[i],end='')
#     i=i-1    

## remove spaces from the string-

# city=input("city name-")
# list=["pune","pali"]
# if city.strip() in list:    ## rstrip-remove right side space
#     print("city present")   ## lstrip----||---left side space
# else:                       ## strip()----||---both side space
#     print(city,"not present")   

## finding substring-
# s='durgasoftdurga soft'
# print(s.find('zz'))
# ## rfind(reverse find)-but in right to left i.e positive index given


# print(s.rfind('u'))

## s.find(substring,begin,end)
# s="durgasolutiondurgasolution"
# print(s.find('a',5,20))

## index method-everything same except -1 index give value error
# s="durgasolutiondurgasolution"
# print(s.index('d'))

# s=input("enter main stream-")
# sbs=input("enter subsring-")
# try:
#     n=s.index(sbs)
# except ValueError:
#     print("sbs not found")
# else:
#     print("sbs found")

# s=input("enter main stream-")
# sbs=input("enter subsring-")
# flag=False
# pos=-1
# n=len(s)

# while True:
#     pos=s.find(sbs,pos+1,n)
#     if pos==-1:
#         break
#     print("found at index:",pos)
#     flag=True
    
# if flag==False:
#     print("Not found")

#### counting character fron subs-
# x="shrishri"
# print(x.count("shri"))

# x="shrishriiiiiiiiiiii"
# print(x.count("i",5,10))

# x="shrishriiiiiiiiiiii"
# print(x.count("i",5,len(x)))

# ## replace str with anothr str-
# s=("shri is goood")
# print(s,id(s))
# s=s.replace("goood","easy")
# print(s,id(s))




# s=("shri",  "mane",  "don")
# e='-'.join(s)
# print(e)

# s="shrib ,mane"  
# e=s.split(',')
# for x in e:
#     print(x)
    
# .check type of character in str -
# s=input("enter any chracter-")
# if s.isalnum():
#     print("alnum cha")
#     if s.isalpha():
#         print("al cha")
#         if s.islower():
#             print("lower case char-")
#         else :
#             print("upper case-")
#     else:
#         print("its digit-")        
# elif s.isspace():
#     print("space char-")
# else:
#     print("non space special cha-")                    

## formatting str-
# name=input("name-")
# age=int(input("age-"))
# salary=int(input("salary-"))
# print("{}'age is {} and his salary is {}".format(name,age,salary))

# s=input("name- ")
# print(''.join(reversed(s)))

# s=input("name- ")
# for x in reversed(s):
#     print(x,end='')
## i=len(s)-1
# output=''
# while i>=0:
#     output=output+s[i]
#     i=i-1
# print(output)    

# s=input("name-")
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# output=' '.join(l1)
# print(output)


# s=input("name-")
# l=s.split()
# l1=[]
# for x in l:
#     l1.append(x[::-1])
# # while i>=0:
# #     l1.append(l[i])
# #     i=i-1
# output=' '.join(l1)
# # print(output)
# print(output)

# # chara at even and odd no-
# 1- using slice-
# s=input("take  str-")
# print("even no=",(s[::2]))
# print("odd no-",(s[1::2]))
# 2- using while loop-

# s=input("str-")
# i=0
# print("even no-")
# while i<len(s) :
#     print(s[i],end=',')
#     i=i+2
# print()    
# print("odd no-")
# i=1
# while i<len(s):
#     print(s[i],end=',')
#     i=i+2

##  Q-  A12B56C84 --->ABC125684

# from numpy import char


# s = "ABC125684"
# num_str = ""
# char_str = ""
# for i in s:
#     # print(i)
#     if i.isdigit():
#         num_str = num_str + i
#     elif i.isalpha():
#         char_str = char_str + i
# print(char_str + num_str)

# s=input("enter str-")
# s1=s2=output=''
# for x in s:
#     if x.isalpha():
#         s1=s1+x
#     else:
#         s2=s2+x
# print(s1+s2)
# print(s1)
# print(s2)
# print(sorted(s1+s2))
# for x in sorted(s1):        ##SORTED=sort in aplhabeically and numerically
#     output=output+x
# for x in sorted(s2):
#     output=output+x
#     output=''.join(x)     
# print(output)             

## mix 2str=
# s1=input("1 str-")
# s2=input("2str-")
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         output=output+s1[i]
#         i+=1
#     if j<len(s2):
#         output=output+s2[j]
#         j+=2
# print(output)            

## Q-a4b3c2---->aaaabbbcc



# s=input("str=")
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x      ###(previous=save str)
#     else:
#         output=output+previous*(int(x)-1)    
# print(output)

## Q-a4k3b2------>aeknbd

# s=input("str-")
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x
#     else:
#         output=output+chr(ord(previous)+int(x))    
# print(output)

## Q-ABCKKKDDDCCVVKKASD------->ABCKDVS
# s=input("int-")
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# output=''.join(l)
# print(output)

# print(''.join(set(s)))

# Q-ABABABABAABCC----->A=6,B=5,C=2

s=input("str-")
d={}
for x in s:
    if x not in d.keys():
        d[x]=1
    else :
        d[x]=d[x]+1    
print(d)
for k,v in d.items():
    print("{} occurs {} times.".format(k,v))












