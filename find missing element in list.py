#print the missing elements in list
'''
a=[4,2,7,1,9,3]
for i in range(0,(max(a)+1)):
    if i not in a:
        print(i)
'''


    
#using list comprehension
'''
a=[4,2,7,1,9,3]
res=[i for i in range(0,(max(a)+1)) if i not in a]
print(res)
'''
