'''
#Print triangle
x = int(input("enter integer b/w 1 to 10: "))
i = 1
while i <= x:
    print(i*'*')
    i += 1
'''

'''
#Print reverse triangle
x = int(input("enter integer b/w 1 to 10: "))
i = 0
while i < x:
    print((x-i)*'*')
    i += 1
'''

'''
#Print sum
x = int(input("enter integer: "))
i = 1
sum = 0
while i <= x:
    sum += i
    i += 1
print("Sum is", sum)
'''

'''
#Print product
x = int(input("enter integer: "))
i = 1
prod = 1
while i <= x:
    prod *= i
    i += 1
print("Prod is", prod)
'''

'''
#Print sum of odd
x = int(input("enter integer: "))
i = 1
sum = 0
while i <= x:
    sum += i
    i += 2
print("Sum of odds is", sum)
'''

'''
#Print sum of x odds
x = int(input("enter integer: "))
i = 1 #counter
odds = 1 #odd numbers
sum = 0

while i <= x:
    sum += odds
    i += 1 #increment counter by one step
    odds += 2 #set the next odd number

print("Sum of odds is", sum)
'''

'''
#Password 3 try
password = '80'
attempts = 3

x = input("Please enter password: ")

while not(attempts == 0):
    y = eval(x)
    if (y%10)%2 == 1 or (y/10)%2 == 1:
        x = input("Invalid password. Try again: ")
        attempts -= 1
    elif not(x == password):
        x = input("Invalid password. Try again: ")
        attempts -= 1
    elif x == password:
        print("Correct Password.")
        break
if not(x == password):
    print("Too many invalid attempts. Come back later")
'''

'''
#reverse digits
n = int(input("enter integer: "))

while n%10 == 0:
    n = int(input("bad n, enter another integer: "))

new = 0
while n > 0:
    new *= 10
    new += n%10
    n //= 10

print("reversed is", new)
'''

'''
#prime check
n = int(input("enter integer greater than 1: "))
i = 2
flag = 0

while i < n and flag == 0:
    if n%i == 0:
        print(n, "is a composite number")
        flag = 1
        
    i += 1

if flag == 0:
    print(n, "is a prime number")
'''

'''
#for sum
n = int(input("integer: "))
sum = 0

for i in range(n):
    sum += i+1

print("sum is", sum)
'''


#sum to 20
for i in range(1, 1001):
    if i%10 + i//10%10 + i//100%10 == 20:
        print(i)
        
