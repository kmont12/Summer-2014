f=open("Default",'r')
out=open("DefaultKD",'w')
for line in f:
    ping=float(line.rstrip())
    result=(-.0009*ping+.45)
    if result>0:
    	out.write(str(result)+"\n")
f.close()
out.close()
    
