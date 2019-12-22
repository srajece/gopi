import re
s=open("test.txt",'r')
for i in s:
    for j in i.split():
        if re.search('offset=',j):
            t=float(j[j.index('=')+1: ])+50
            print(t)
            
