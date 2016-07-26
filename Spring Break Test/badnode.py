import subprocess
f=open("nodeIP",'r')
out=open("badnodes",'w')
for line in f:
    try:
        response = subprocess.check_output("ping -c 1 "+ line.rstrip() +" | grep from", shell=True).split("=")[3].split()[0]
    
        float(response.rstrip())
    except:
        out.write(line.rstrip()+"\n")
f.close()
out.close()
