'''
k={1:["c","a","b"],2:["f","d","e"],7:['s','p','q','r'],9:['w','x','y','z']}
keypad=int(input("enter the keypad"))
c=int(input("no of clicks"))

if keypad==7 or keypad==9:
    print(k[keypad][c%4])
else:
    print(k[keypad][c%3])
'''

'''sn=input("Enter the starting number")
en=input("Enter the ending number")'''
'''
a=[]
c=0
for num in range(2,100):
    for dnum in range(1,num):
        if (dnum>1):
            if (num % dnum ==0):
                break
    else:
        a.append(num)
        c+=1
        if c==10:
            break
print(a)
print(c)
'''        
        
        
    
    
