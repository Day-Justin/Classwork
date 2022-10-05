'''
#reverse order
x = [3,5,2,56,7,5,27,8,34]
x.sort()
print(x)

y = x[::-1]
print(y)

z = []
for i in range(len(x)):
    z.append(x[-(i+1)])
print(z)

for i in range(len(x)//2):
    x[i],x[-(i+1)] = x[-(i+1)], x[i]
print(x)
'''

'''
#passing fxn

def line(x):
    return (x)

def integrate(fxn,a,b):
    integral = 0
    increment = .00001

    while a <= b:
        integral += increment * fxn(a)
        a += increment

    return integral

print(integrate(line,0,10))
'''

'''
#printf
for i in range(3):
    for j in range(3):
        print(f"   {i+j"), end = ' ')
    print()
'''

'''
#4x4 array
a=[] 
for i in range(4):
    a.append(4*[0])

print(a)
'''

from random import randint, random

n = int(input('n: '))
m = int(input('m: '))

x = []

for i in range(n):
    ran = randint(1,m)
    while ran in x:
        ran = randint(1,m)
    x.append(ran)

print(x)

