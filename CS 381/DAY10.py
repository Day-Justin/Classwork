from random import randint

'''
n = int(input('n: '))
m = int(input('m: '))
x = []

for i in range(n):
    ri = randint(1,m)

    while ri in x:
        ri = randint(1,m)

    x.append(ri)

print(x)
'''

'''
#m*n using set
n = int(input('n: '))
m = int(input('m: '))
k = int(input('k: '))
x = []
s = set()

while k <= m*n:
    k = int(input('something bigger than n*m please: '))

for i in range(n):
    x.append(m*[0])

for i in range(n):
    for j in range(m):
        ri = randint(1,k)

        while ri in s:
            ri = randint(1,k)

        x[i][j] = ri
        s.add(ri)

for i in range(n):
    for j in range(m):
        print(f'{x[i][j] : >6d}', end = '')
    print()

# can also first populate the set with range of random, and then pop into the matrix
'''


#get row
def get_row(x,i):
    y = []
    for j in range(i):
        y.append(x[i-1][j])
    return y

#get column
def get_col(x,i):
    y = []

    for j in range(i):
        y.append(x[j][i-1])

    return y

#et sum of main diagonal
def sumDiag(x):
    sumD = 0

    for i in range(len(x)):
        sumD += x[i][i]

    return sumD
    

#get sum minor diagonal
def sumMinor(x):
    sumM = 0
    for i in range(len(x)):
        sumM += x[i][-(i+1)]
    
    return sumM


#list comprehension
a = [x**2 for x in range(1,101) if x % 2 == 0]

x = [1,2,3]
y=[10,11,12]

z = sum([x[i]*y[i] for i in range(len(x))])
