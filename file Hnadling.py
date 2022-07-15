# a=open('abcd.py','r')
# print("File name:",a.name)
# print("File Mode:",a.mode)
# print("File readable:",a.readable())
# print("File writable:",a.writable())
# a.close()
# print("File close:",a.closed)
 
# list=['shri\n','mane\n','assx\n','durgfa\n']
# a.writelines(list)
# print("ok")

# data=a.read()
# print(data)

# data=a.read(10)
# print(data)

# list=a.readlines()
# for line in list:
#     print(line)

# with open('abcd.py','w') as a:
#     a.write("mane brand \n")
#     a.write("shri brand\n")
#     a.write("djbjdvb")

# a=open('abcd.py',"r")
# print(a.tell())
# print(a.read(3))
# print(a.tell())
# print(a.read(2))

# data="all students stupids"
# f=open('abcd.py','w')
# f.write(data)
# with open('abcd.py','r+') as f:
#     x=f.read()
#     print(x)
#     f.seek(17)
#     print("current cursor pos=",f.tell())
#     f.write("GEMS!!!")
#     f.seek(0)
#     x=f.read()
#     print("data after modification:")
    # print(x)

# import os
# fname=input("enter file name:")
# if os.path.isfile(fname):
#     print("file exists:",fname)
#     f=open(fname,'r')
#     print("the content of file is:")
#     x=f.read()
#     print(x)
# else:
#     print("file not exists:",fname)

# import os,sys
# fname=input("enter file name:")
# if os.path.isfile(fname):
#     print("file exists:",fname)
#     f=open(fname,'r')
# else:
#     print("file not exists:",fname)
#     sys.exit(0)
# lcount=wcount=ccount=0
# for line in f:
#     lcount=lcount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# print("no of lines=",lcount)
# print("no of words=",wcount)
# print("no of chara=",ccount)

# f1=open("trying.py",'rb')
# f2=open("sss.jpg",'wb')
# bytes=f(iin")

# from zipfile import*
# f=ZipFile("files1.zip",'w',ZIP_DEFLATED)
# f.write("cricke.txt")
# f.close()
# print("ok")

# import os
# cwd=os.getcwd()
# print(cwd)

# import os
# os.mkdir("mkdir")
# print("ok")

# import os
# os.mkdir("mkdir/pypract")
# print("ok")

## walk() = to know content in subdir-

# import os
# from datetime import*
# stats=os.stat("log.txt")
# print(stats)
# print(datetime.fromtimestamp(stats.st_atime))
 
# s=[1,2,3]
# a=[x+1 for x in s]
# print(a)

# s=[[1,5],[3,4],[5,6]]
# a=[]
# a=[x[0] for x in s]
# print(a)

# s=[[1,5],[3,4],[5,6]]
# for i in s:
#     w=i[0]
#     a.append(w)
# print(a)

# list=[[1,2,3,4,100],[5,6,7,8,9,200],[14,252,35,300]]
# p=[x[-1] for x in list ]
# print(p)


# list=[[1,2,4,6,10],[3,4,4,20],[5,6,4,4,7,4,9,30]]
# w=[]
# for i in list:
#     e=i[2]
#     w.append(e)
# print(w)

# import pickle
# class employee:
#     def __init__(self,eno,ename):
#         self.x=eno
#         self.y=ename
#     def display(self):
#         print(self.x,"\t",self.y,"\t")
# with open("emp.data.py","wb") as f:
#     e=employee(1212,"shri")
#     pickle.dump(e,f)
#     print("dump ok")

# with open("emp.data.py","rb") as f:
#     obj=pickle.load(f)
#     print("unpickle ok")
#     obj.display()
#     print(obj) 
n=int(input("emp")) 
for i in range(n):
    eno=int(input("emp no="))
    ename=input("name=")
































