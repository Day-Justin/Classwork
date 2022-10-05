
#max range
def getmax(x,i): #x is list, i int
    #get max from x among first i elemnts

    maxNum = x[0]
    pos = 0

    '''
    for j in range(0,i):
        if x[j] > maxNum:
            maxNum = x[j]
            pos = j
    '''

    for j in x[:i]:
        if j > maxNum:
            maxNum = j

    return maxNum, x.index(maxNum)

'''
#Sieve of Eratosthenes 
x=[] 
for i in range(101): 
    x.append(i) 

primes=[2] 
x[0]=x[1]=x[2]=0 
p=2 # the first prime 

while sum(x) != 0: # as long as sum(x)!=0, there are still non-zero entries in x. 
    # Zero out all multiples of p 
    i=1 

    while i*p<=100: 
        x[p*i]=0 
        i=i+1 

    # Now, look for the next prime 
    p=p+1 
    while x[p]==0: # it’s at the next non-zero position of x 
        p=p+1 

    # We found it. Add it to the list of primes, and zero out its position in x 
    primes.append(p)
    x[p]=0 

# Done! Now print the list of primes. 
print(primes)
'''

'''
#Interview question monte carlo 
from math import sqrt 
from random import random 

count=0
for i in range(1000000): 
    x=random()
    y=random() 

    if sqrt(x*x+y*y)<1: 
        count+=1
        
print(4*(count/1000000))
'''

#unpacking
def addem(*x):
    return sum(x)

#selection sort
def select_sort(x): 
    for i in range(len(x)-1): 
        y=x[i:] # each time through the loop look for the minimum from position i to the end. 
        m=min(y) 
        pos=x.index(m,i,len(x)) # find the index of the first element with value m in the range [i,len(x) ) 
        x[i],x[pos]=x[pos],x[i] # swap the element at position i with the element at position pos 

#a= [4,2,7,1,45,23]
#select_sort(a)



print(a)

