import networkx as nx
import pandas as pd
import numpy as np
import os
from statistics import mode,mean
from collections import Counter

user2uid={}
uid2user={}

aliases="/mnt/a99/d0/jagadeesha/ts_feb/user_uid_snapshot_out.csv"
f=open(aliases,"r")  
# lines=f.readlines()

for l in f:
    l=l.strip()
    user,uid=l.split(",")
    uid=int(uid)
    user=user.lower()
    user2uid[user]=uid
    uid2user[uid]=user
f.close()


members={"BJP":[],
        "INC":[]}

aliases="/mnt/a99/d0/jagadeesha/ts_feb/user_id_party.csv"
f=open(aliases,"r")

for l in f:
    l=l.strip()
    user,uid,party=l.split(",")
    uid=int(uid)
    user=user.lower()
    user2uid[user]=uid
#     uid2user[uid]=user
    members[party].append(uid)
# lines=f.readlines()
f.close()


csvfile="/mnt/a99/d0/jagadeesha/ts_feb/rtid_tid_from_to_all.csv"
df=pd.read_csv(csvfile,  , 'rtid': object,'from': object, 'to': object})


froms=df["from"].unique().tolist()
tos=df["to"].unique().tolist()


s=set()


s.update(froms)
s.update(tos)


edges={}

aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_fr.csv"
f=open(aliases,"r")
count=0
for l in f:
    l=l.strip()
    from_, to_=l.split(",")
    try:
        from_=int(from_)
        to_=int(to_)
        if (from_ in s) and (to_ in s):
            edges[(from_,to_)]=1
    except:
        print(count, from_, to_)
    count+=1
    if count%100000000==0:
        print(count)
f.close()

aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_fg.csv"
f=open(aliases,"r")
count=0
for l in f:
    l=l.strip()
    from_, to_=l.split(",")
    try:
        from_=int(from_)
        to_=int(to_)
        if (from_ in s) and (to_ in s):
            edges[(from_,to_)]=1
    except:
        print(count, from_, to_)
    count+=1
    if count%100000000==0:
        print(count)
f.close()


aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_p.csv"
f=open(aliases,"r")
count=0
for l in f:
    l=l.strip()
    from_, to_=l.split(",")
    try:
        from_=int(from_)
        to_=int(to_)
        if (from_ in s) and (to_ in s):
            edges[(from_,to_)]=1
    except:
        print(count, from_, to_)
    count+=1
    if count%100000000==0:
        print(count)
f.close()


aliases="/mnt/a99/d0/jagadeesha/ts_feb/edges_user_fg.csv"
f=open(aliases,"r")
count=0
for l in f:
    l=l.strip()
    from_, to_=l.split(",")
    try:
        from_=int(from_)
        to_=int(to_)
        if (from_ in s) and (to_ in s):
            edges[(from_,to_)]=1
    except:
        print(count, from_, to_)
    count+=1
    if count%100000000==0:
        print(count)
f.close()


import pickle()


