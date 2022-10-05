import DAY5

#print primes
def prime_range(x,y):
    count = 0
    
    for i in range(x,y+1):
        if is_prime(i):
            print(i, end = ' ')
            count += 1

            if count > 4:
                print()
                count = 0


#sum of digits
def sum_of_digits(n):
    sum = 0

    while n > 0:
        sum += n%10

        n = n//10

    return sum

#my_bin
def my_bin(n):
    bin = ''

    while n > 0:
        bin = str(n%2) + bin
        
        n //= 2

    return bin

'''
#list sum
l = []

for i in range(10):
    l.append(i+1)

sum = 0
for i in l:
    sum +=i

print(sum)
'''

'''
#list sum
l = []

for i in range(10):
    l.append(i+1)

SUM = 0
for i in range(0, len(l), 2):
    SUM += l[i]

print(SUM)
print(sum(l))
'''

from random import random, randint

'''
#rand 1-10
s=[]
max1 = 0
loc1 = 0
for i in range(10):
    x = randint(1,10)

    if x > max1:
        max1 = x
        loc1 = i

    s.append(x)

max2 = 0
loc2 = 0
for i in s:
    if i > max2:
        max2 = i
    loc2 = s.index(max2)

print(s)
print(max1)
print(loc1)
print(max2)
print(loc2)
'''


