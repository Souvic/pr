import networkx as nx
import pandas as pd
import numpy as np
import os
G = nx.MultiDiGraph()

aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_reply_2.csv"
# aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_retweet_2.csv"
f=open(aliases,"r")
count=0
for l in f:
    l=l.strip()
    from_, to_=l.split(",")
    try:
        from_=int(from_)
        to_=int(to_)
        G.add_edge(from_,to_)
    except:
        print(count, from_, to_)
    count+=1
    if count%500000==0:
        print(count)
f.close()

print("___________")

nx.write_gexf(G,"Gy.gexf")


# aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_retweet_2.csv"
f=open(aliases,"r")
count=0
for l in f:
    l=l.strip()
    from_, to_=l.split(",")
    try:
        from_=int(from_)
        to_=int(to_)
        G.add_edge(from_,to_)
    except:
        print(count, from_, to_)
    count+=1
    if count%500000==0:
        print(count)
f.close()

print("___________")

nx.write_gexf(G,"Gt.gexf")
