import os, subprocess


out=open("nodeIP",'r')

for line in out:
    os.chdir(line.rstrip())
    subprocess.call("touch goodnodes",shell =True)
    os.chdir("..")


    

out.close()
