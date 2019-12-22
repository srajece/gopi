'''
def add(a,b,d):
    c=a+b+d
    return c
def sub(a,b):
    c=a-b
    return c
if __name__=="__main__":
    print(add(5,d=3,b=7))
    print(sub(b=8,a=3))
'''

'''
def fun(*arg):
    
    print(arg)
fun(1,2,3,4,5)
'''

'''
list1=[1,2,3,4]
fun(*list1)
'''

'''
d={"a":"gopi","b":'kumar',"c":"ram","d":"yuvi"}
fun(**d)
'''

'''
def add(*arg):
    sum1=0
    for i in arg:
            sum1=sum1+i
    return sum1
print(add(1,2,4,6))
'''

