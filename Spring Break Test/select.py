import os

count=0

for i in range(1,10138):
    os.chdir(str(i))
    f1=open("defaultTrace",'r')
    f2=open("detourTrace",'r')
    f3=open("selectionTrace",'r')
    line=f2.readline()
    try:
        count+=1
    except:
        pass
    os.chdir("..")
print count/10138.

