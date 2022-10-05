from random import randint

def get_col(x,i):
    return [x[j][i] for j in range(len(x))]

def sum_col(x,i):
    return sum(get_col(x,i))

'''
#sum col
a = []
for i in range(4):
    a.append(4*[0])

for i in range(len(a)):
    for j in range(len(a)):
        a[i][j] = randint(1,50)

print(f'{a}\n{sum_col(a,3)}')
'''


#generator and yied
#a generator using yield keyword will create a generator class object that is also iterable
def countdown(n):
    print('Countdown from', n)
    while n>0:
        yield n #fxn is called once, but it returns an iterable, and yield members where it last yielded, and continues with the fxn
        n -= 1
'''
for x in countdown(10):
    print('T-minus', x)
    
c = countdown(10)
#>>>c
#<generator object countdown at 0xlocation
#it created a generator object, instead of executing because generators only excutes if u iterate on it

next(c)
#iterates to the next elemnt, and works becasue its iterating on the generator object

#can also use fxns like sum() on the function
#it knows to stop with stop iteration exception
'''


#leapyear generator
def leapyear():
    n = 4
    while True: #n < 2024
        yield n
        n += 4
        if n % 100 == 0 and n % 400 != 0:
            n += 4

#fib generator
def fib():
    x = 0
    y = 1
    yield y

    while True:
        x, y = y, (x+y)
        yield y

#prime generator
def is_prime(x):
    p = True
    for i in range(int(x**.5)):
        if x % i == 0:
            p = False
            break

    return p

def prime_gen():
    p = 3
    yield 2

    while True:
        if is_prime(p) is False:
            p += 2
            continue
        else:
            yield p
            p += 2

'''
decoratoors
fxn wrapping around another fxn that alter or changes behavior and apperance of wrapped fxn
'''

from functools import wraps

def trace(func): #takes the func as a arg
    @wraps(func)
    def call(*args, **kwargs): #does the decorative stuff
        print('Calling', func.__name__) #decorative arg
        return func(*args, **kwargs) #doing the actual func
    return call # exit out of wrap

@trace
def square(x):
    return x*x

#matrix addition
def add(a,b):
    lena = len(a)
    #x = lena*[lena*[0]]
    x = [lena * [0] for i in range(lena)]

    for i in range(lena):
        for j in range(lena):
            x[i][j] = a[i][j] + b[i][j]

    return x

x = [[1,1],[3,5]]
y = [[1,1],[1,1]]
'''
c = add(x,y)
print(c)
'''

#matrix mult
def mult(a,b):
    lena = len(a)
    lenb = len(b[0])
    x = [lenb * [0] for i in range(lena)]

    for i in range(lena):
        for j in range(lenb):
            x[i][j] = sum([a[i][h] * get_col(b,j)[h] for h in range(len(a[i]))])

    return x

c = mult(y,x)
print(c)
