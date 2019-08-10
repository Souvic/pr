import sys
u=sys.argv[1]
xx=u.split("/")[-1]
hh=open(xx,"w")
oo=0
for i in open(u,"r"):
    hh.write(str(i))
    if(oo==10000):
        break;
    else:
        oo=oo+1
hh.close()
