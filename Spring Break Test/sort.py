import os
outdefault=open("Default","w")
outselection=open("Detour",'w')
outmessage=open("Selection",'w')
count=0

for i in range(1,10138):
    os.chdir(str(i))
    f1=open("defaultTrace",'r')
    f2=open("detourTrace",'r')
    f3=open("selectionTrace",'r')
    for line in f1:
        try:
            x=float(line.rstrip())
            outdefault.write(str(x)+"\n")
        except:
            pass
    for line in f2:
        try:
            x=float(line.rstrip())
            outselection.write(str(x)+"\n")
        except:
            pass
    for line in f3:
        count+=1
    outmessage.write(str(count)+"\n")
    count=0
    os.chdir("..")

outdefault.close()
outselection.close()
outmessage.close()