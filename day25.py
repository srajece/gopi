#Write a Python program to check if a given positive integer is a power of three.
'''
n=int(input("Enter the value: "))
while n%3==0:
    n/=3
if n==1:
    print("True")
else:
    print('False')
'''

#Write a Python program to check if a given positive integer is a power of two.
'''
n=int(input("Enter the value: "))
while n%2==0:
    n/=2
if n==1:
    print("True")
else:
    print('False')
'''

#Write a Python program to check if a given positive integer is a power of Four.
'''
n=int(input("Enter the value: "))
while n%4==0:
    n/=4
if n==1:
    print("True")
else:
    print('False')
'''

#Write a Python program to find a missing number from a list.

n=[int(i) for i in input("Enter the value:").split(' ')]

for i in range(len(n)):
    if i not in n:
        print(i)
