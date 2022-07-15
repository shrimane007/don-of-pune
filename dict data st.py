
### key - values pair=
# d={}   empty dict
# d=dict() empty dict
# d[key]=value
# d={}
# d[100]= 'shri'
# d[200]='durga'
# d[400]='mane'
# d['rich']='soft'
# print(d)

# d={'a':100,'c':200,'j':300}
# print(d)

## add inputs=
# rec={}
# n=int(input("no of students-"))
# i=1
# while i<=n:
#     name=input("student name=")
#     marks=int(input("marks="))
#     rec[name]=marks
#     i+=1
# print("name of student","\t","% marks")
# print()
# for x in rec:
#     print("\t",x,"\t\t",rec[x])   
 
##addd key

# d={key1:value1,key2:value2}
# d={101:'shri',102:'mane',103:'dada'}
# d[104]='sarkar'
# print(d)
# d[101]='bhai'
# print(d)

## del key

# d={101:'shri',102:'mane',103:'dada'}
# del d[101]
# print(d)

# d={101:'shri',102:'mane',103:'dada'}
# d.clear()
# print(d)

# list=['shri','dada','hakaka']
# d1={100:list}
# print(d1)

# d=dict([[100,'shri'],])
# print(d)

# d=dict([[100,'shri'],])
# print(len(d))

# d=dict([[100,'shri'],])    ## get correspoonding value of key
# print(d.get(100))

# d=dict([[100,'shri'],])
# print(d.get(400))        ## doesont get errror

# d=dict([[400,'shri'],])
# print(d.get(400,'mane'))  ## get deefault value

# d=dict([[100,'shri'],[200,'ravi']])
# print(d.pop(100))
# print(d)

# d=dict([[100,'shri'],[200,'ravi']])
# print(d.popitem())
# print(d)

# d=dict([[100,'shri'],[200,'ravi']])
# print(d.keys())
# for x in d.keys():
#         print(x)

# d=dict({100:'shri',200:'ravi'})
# print(d.values())
# for x in d.values():
#         print(x)

# d={100:'shri',200:'ravi'}
# list=d.items()
# for k,v in d.items():
#     print(k,"...",v)
# # print(list)
# print(d.keys())
# for x in d.keys():
#         print(x)

# d=dict([[100,'shri'],[200,'ravi']])
# d1=d.copy()
# print(d1)

# d=dict([[100,'shri'],[200,'ravi']])
# print(d.setdefault(100,'sunny'))    ## give old value instead of new value
# print(d)
  
# d=dict([[100,'shri'],[200,'ravi']])
# d1={'a':100,'b':400}
# d.update(d1)            ## only dict type update
# print(d)

# Q-- Take dict and give sum of values---
# d=eval(input('dict='))
# s=sum(d.values())
# print("sum=",s)

# Q--NO of occurence of given letters in str--->

# d=input("word=")
# s={}
# for x in d:
#     s[x]=s.get(x,0)+1
# print(s)
# print(len(d))

# word=input("word=")
# s={}
# for x in word:
#     s[x]=s.get(x,0)+1
# print(s)
# print("word lenght=",len(word))

# word=input("word=")
# s={}
# for x in word:
#     s[x]=s.get(x,0)+1
# # for k,v in s.items():
# #     print(k,"occured -",v,"times.")
#      ## or
# for k,v in sorted(s.items()):
#     print("{} occured {} times".format(k,v))     

## Q-- find no of vowels in str-->

# word=input("word-")
# s={'a','e','i','o','u'}
# a={}
# for x in word:
#     if x in s:
#        a[x]=a.get(x,0)+1
# for k,v in a.items():
#     print(k, "vowel=" ,"present times-" ,v)     

# Q-- STUDENT NAME AND MARKS IN DICT FORM---->

# n=int(input("no of students-"))
# d={}
# for i in range(n):
#     name=input("student name-")
#     marks=input("marks of student-")
#     d[name]=marks
# while True:
#     name=input("enter student name to get marks-")
#     marks=d.get(name,-1)
#     if marks ==-1:
#         print("student not found.")
#     else:
#         print("marks of student-{} is {}".format(name,marks))    
#     option=input("Do you want to get another student marks?[Yes/No]")
#     if option=="No"or "no":
#         break
# print("Thanks for using our application @@***@@")

# comprehension-
# s={x:x*x for x in range(1,11)}
# print(s)

## zip type=

# s=['a',20,22,30]
# t=[40,50,44,56]
# w=dict(zip(s,t))
# print(w)
 
# s=['a',20,22,30]
# t=[40,50,44,56]
# w=list(zip(s,t))
# print(w)
 


















