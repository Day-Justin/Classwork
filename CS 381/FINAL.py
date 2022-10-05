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
f(2)
'''

'''
n = 150
x = []
for j in range(1, n+1):
    x.extend(str(j))
    print(x)
    x = []
'''

n = [['Justin' ,'Day'], ['Jerry', 'Waxman']]

def lastThenFirst(x):
    return


#x = [[2,3,4],[1,3,2],[5,5,5]]

def max_row_col(x):
    maxx = x[0][0]
    row = 0
    col = 0

    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j] >= maxx:
                maxx = x[i][j]
                row = i
                col = j

    return (maxx, row, col)

#print(max_row_col(x))


from functools import wraps

def trace(func): #takes the func as a arg
    @wraps(func)
    def call(*args, **kwargs): #does the decorative stuff
        print('Calling', func.__name__) #decorative arg
        return func(*args, **kwargs) #doing the actual func
    return call # exit out of wrap

def oddEven(m,n):
    odd = True
    startOdd = True
    
    if m % 2 == 0:
        startOdd = False 

    while True: # odd section
        if startOdd == True:
            x = m
        else:
            x = m + 1
            
        while odd == True:
            if x > n:
                odd = False
                pass
            else:
                yield x
                x += 2

        if startOdd == True:
            x = m + 1
        else:
            x = m

        while odd == False: #even section
            if x > n:
                odd = True
                pass
            else:
                yield x
                x += 2
                
    

'''
z = [1,2,3,2,1,2,4,5,1,4,1]

d = {}

for i in range(len(z)):
    if z[i] not in d:
        d[z[i]] = []
        d[z[i]].append(i)
    else:
        d[z[i]].append(i)

for i in d:
    print(f'Element: {i}, found {len(d[i])} times, at positions ', end = '')
    for j in range(len(d[i])):
        print( d[i][j], end = '')
        if j < len(d[1])-1:
            print(',', end = ' ')
    print()
'''

grades = [60,345,3463,3,67,34,567,2]

def get_nth_largest(grades,n):
    return sorted(grades)[-n]

#print(get_nth_largest(grades, 3))

def lastFirst(x):
    return sorted(x, key = lambda x : x[][]
