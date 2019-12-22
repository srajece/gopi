#file operation (replace the content in file)

'''
s=open('test.txt').read()
s=s.replace('Theenathayalan','Rajkumar')
f=open('test.txt','w')
f.write(s)
f.close()
'''

#file operation

import re
s=open('test2.txt','r')
for i in s:
    p=(re.findall("offset=\w+.\w+",i))
    for j in p:
        print(j)
        p1=j.split('=')        
        p2=float(p1[1])+50
        a=i[ : i.index("offset=")+len("offset=")]+str(p2)+ i[i.index('offset=')+len('offset=')+len(j):]
        print(a)
        
       

'''
s="abc=2981362 kahdkhas=736299 offset=182.69 kfhe=123t1 "
newvalue='250.9888888888'
print(s[ : s.index("offset=")+len("offset=")]+newvalue+ s[s.index('offset=')+len('offset=')+len(newvalue):])
'''
