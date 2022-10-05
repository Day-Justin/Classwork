'''
numgrade = int(input('num'))
if numgrade <= 100:
    letgrade = 'a'
elif numgrade < 90:
    letgrade = 'b'
elif numgrade < 80:
    letgrade = 'c'
elif numgrade < 70:
    letgrade = 'd'
elif numgrade < 60:
    letgrade = 'f'
print(letgrade)
'''

'''
for i in range(2):
    for j in range(3):
        print(i,j)
'''    

'''
def f(n):
    for i in range(1, n+1):
        print((n-i)*' ', 2*i*'*', (n-i)*' ', sep = '')
        
'''

'''
def VNN(n):
    x = []
    for i in range(1,n):
        if n % i == 0:
            x.append(i)

    print(sum(x) == n)
'''

'''
x = [1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17]

def f(x):
    for i in range(0,len(x)//2):
        x[i], x[-(i+1)] = x[-(i+1)], x[i]
    return x

print(f(x))
'''

#'''
x = [4,3,2,1,1,2,6]

def remove_duplicates(x):
    y = []
    minx = min(x)
    maxx = max(x)

    while minx <= maxx:
        y.append(minx)
        print(y)
        minx +=1
        while not(minx in x) or minx > maxx:
            minx += 1
    return y

print(remove_duplicates(x))
#'''
#'''
def amount(feet):
    handout = 0
    leftover = feet
    
    if leftover > 2000:
        count = leftover - 2000
        leftover = 2000
        handout += .20 * count
        print(handout, leftover)

    if leftover > 1000:
        count = leftover - 1000
        leftover = 1000
        handout += .15 * count
        print(handout,leftover)

    if leftover > 100:
        count = leftover - 100
        leftover = 100
        handout += .10 * count

    return handout
#'''

'''
def is_prime(n):
    prime = True
    for i in range(2,n):
        if n % i != 0:
            prime = False
            break
    return prime

for i in range(3,1000,2):
    if is_prime(i) and is_prime(i+2):
        print(i, i+2)
'''

'''
def f(n):
    x = []
    for i in range(n):
            x.append(i)
            print(x)
            x.append([i])
            print(x)
            x.append(i)
            print(x)
f(3)
'''

'''
def f(x,n):
    return int(str(x)[n-1])
'''

'''
def diagDiff(x,y):
    green = []
    orange = []
    for i in x[:y*y+1:y+1]: #for the main diagonal, it starts at the first element and then every other one is y+1 elements away
        print(i)
        green.append(i)
    for i in x[y-1:y*y-1:y-1]: #for the minor diagonal, it starts at y, and is y -1 aawy but since 
        print(i)
        orange.append(i)

    sumg = sum(green)
    sumo = sum(orange)
    print(sumg)
    print(sumo)
    return sumg-sumo

x = [1,2,3,4,5,6,7,8,9]
print(diagDiff(x,3))
'''

'''
def f(p,n,*x):
    sum = 0
    for i in x[:n]:
        sum +=i
    avg = sum /n
    return(p,n,x,avg)
'''
