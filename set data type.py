# s=set()
# print(type(s))

# l=[10,20,30,40,50,40,10,20]
# s=set(l)
# print(s)

# s=set('gghhjjjjhgg')
# print(s)

# s={1,2,3}
# s.add(20) #add only take only one arg
# print(s)

# s={10,30,50,70}
# l=[20,40,60,80,10,50]
# s.update(l,range(1,5),'durga')  #update gets only sequence value bu not sinle value
# print(s)

# s={10,30,50,70}
# s1=s.copy()         ## aliacing
# print(s1)

# s={10,30,50,70}
# print(s.pop())    ## random element removed

# s={10,30,50,70}
# s.remove(10)    #ker error gives if another no put
# print(s)

# s={10,30,50,70}
# s.discard(10)    # if element nott here then not give any error
# s.discard (120)
# print(s)

# s={10,30,50,70}
# s.clear()       #clear all element.
# print(s)
 
### mathematical operations-

# ## union= use x.union(y) or x|y
# s={10,30,50,70}
# t={50,70,10,30,40}
# print(s.union(t))
# ##or
# print(s|t)

## intersection= use x.intersection9y or x&y
# s={10,30,50,70}           ## take only common element
# t={50,70,10,30,40}
# print(s.intersection(t))
# #or
# print(s&t)

## difference-use x.difference(y) or x-y

# s={10,30,50,70,80,100}
# t={50,70,10,30,40}
# print(s.difference(t))
# #or
# print(s-t)

## symmetric _ difference/ x^y= elem in x or y but not in both=
# only uncommon factors
# s={50,70,10,30,40}
# t={50,70,10,30,40,400}
# print(s.symmetric_difference(t))
# #or
# print(s^t)

# v={50,70,10,30,40}
# print(10 in v)

####### set comprehension---

# s={x*x for x in range(1,11)}
# print(s)

## index and slic not applicable because order not mntn in set

## eliminate duplicates from list=
# l=eval(input("list="))
# s=set(l)
# print(s)

# l=eval(input("list="))
# l1=[]
# for x in l:
#     if x not in l1:
#         l1.append(x)
# print(l1)

## diff vowels in str=

# s=input("word=")
# r=set(s)
# v={'a','e','i','o','u'}
# d=r.intersection(v)
# print("vowel word=",d,"no =",len(d))





 