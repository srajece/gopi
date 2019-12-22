#median in list
'''
a=[2,5,7,4,3]
a.sort()
length=len(a)
mid=length//2
print(mid)
result=(a[mid]+a[~mid])/2
print(result)
'''


#using statictics module
'''
import statistics
a=[2,4,6,3,9]
res=statistics.median(a)
print(res)
'''
