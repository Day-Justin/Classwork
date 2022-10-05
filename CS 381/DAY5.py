'''
#first 100 primes
for i in range(2, 101):
    prime = True
    n = 2

    while n <= i**(.5) and prime:
        if(i % n == 0):
            prime = False
        n += 1

    if prime:
        print(i, "is a Prime")
'''

'''
#print matrix grid
for i in range(1,5):
    for j in range(1,5):
        print('(', i, ',', j, ')', end = ' ')

    print('')
'''

'''
#print # tirangle
for i in range(1,10):
    print(i*' ', end = '')
    
    for j in range(i,10):
        print(j, end = '')

    for j in range(8, i-1, -1):
            print(j, end = '')

    print()
'''


#is even
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

#print(is_even(int(input("integer: "))))



#leap year
def is_leap(x):
    if x % 100 == 0 and x % 400 != 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False



#is prime
def is_prime(x):
    prime = True

    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            prime = False
            break

    return prime



#prime in range
def prime_range(x,y):
    count = 1
    
    for i in range(x, y +1):
        if is_prime(i):
            print(i, end = ' ')
            if count > 4:
                print()
                count = 0
            count += 1
        
    
