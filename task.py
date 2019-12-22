import re
s=open('test.txt','r')
print(s)
for i in s:
    print(i)
    for j in i.split():
        print(j)
        if re.search('offset=',j):
            t=float(j[j.index('=')+1:])+50.5
            t='offset='+str(t)
            f=open('test1.txt','a')
            f.write(t)
            f.write(' ')        
            
        else:
            f=open('test1.txt','a')
            f.write(j)
            f.write(' ')
    f=open('test1.txt','a')
    f.write('\n')
f.close()
