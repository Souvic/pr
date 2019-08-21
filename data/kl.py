import pandas as pd
import numpy as np
import json
import os
G=dict()
#aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_reply_2.csv"
aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_retweet_2.csv"
f=open(aliases,"r")
count=0
for l in f:
    l=l.strip()
    from_, to_=l.split(",")
    try:
        from_=int(from_)
        to_=int(to_)
        try:
        	try:
        		G[from_][to_]=G[from_][to_]+1
        	except:
        		G[from_][to_]=1
        except:
        	G[from_]=dict()
    except:
        print(count, from_, to_)
    count+=1
    if count%500000==0:
        print(count)
f.close()
print("___________")
json.dump(G,open("Gt.json","wb"))



