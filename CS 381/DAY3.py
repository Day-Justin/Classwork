'''
#if even or odd
x = eval(input("Please enter an integer: "))
#if x%2 == 0:
#    print(x, "is even.")
#if x%2 == 1:
#    print(x, "is odd.")
ans= 'odd'
if x%2 == 0:
    ans = 'even'
print(ans)
'''

'''
#1,2,3
x = eval(input("Enter 1, 2, or 3: "))
out = 'ERROR'
if x == 1:
    out = 'red'
if x == 2:
    out = 'green'
if x == 3:
    out = 'blue'
print(out)
'''

'''
#range
x = eval(input("Enter number 1-30: "))
out = 'ERROR'
if 1<=x<=10:
    out = 'red'
if 11<=x<=20:
    out = 'green'
if 21<=x<=30:
    out = 'blue'
print(out)
'''

'''
#max 2 num
x = eval(input("enter first integer: "))
y = eval(input("enter second integer: "))
if x > y:
    print(x)
else:
    print(y)
'''

'''
#max 3 num
x = eval(input("enter first integer: "))
y = eval(input("enter second integer: "))
z = eval(input("enter third integer: "))
if x >= y and x >= z:
    print(x)
if y >= x and y >= z:
    print(y)
else:
    print(z)
'''

'''
#max 5 num
v = eval(input("enter first integer: "))
w = eval(input("enter second integer: "))
x = eval(input("enter third integer: "))
y = eval(input("enter fourth integer: "))
z = eval(input("enter fifth integer: "))

if v >= w and v >= x and v >= y and v >= z:
    print(v)
if w >= x and w >= y and w >= z:
    print(w)
if x >= y and x >=z:
    print (x)
if y >= z:
    print(y)
else:
    print(z)

n = int(input("enter number 1: "))
a = int(input("enter number 2: "))
if a > n:
    n = a
a = int(input("enter number 3: "))
if a > n:
    n = a
a = int(input("enter number 4: "))
if a > n:
    n = a
a = int(input("enter number 5: "))
if a > n:
    n = a
print(n)
'''

'''
#reformat
x = 9
y = 8
z = 7
if x > 9:
    if y > 8:
        print ("x > 9 and y > 8")
    else:
        if z >= 7:
            print("x <= 9 and z >= 7")
        else:
            print("x <= 9 and z < 7")            
'''

'''
#grades
n = eval(input("grade: "))

if n >= 90:
    print('A')
elif n >= 80:
    print('B')
elif n >= 70:
    print('C')
elif n >= 60:
    print('D')
else:
    print('F')
'''

'''
#4d palindrome
n = int(input("number: "))

if n < 1000 or n > 9999:
    print('Number out of range')

elif n//1000 == n%10 and (n%1000)//100 == (n%100)//10:
    print('Palindrome')

else:
    print('Not Palindrome')
'''

'''
#coin change
x = eval(input("Total change: "))
x *= 100 #bring the coins value out of decimals
x = int(x % 100) #now n is only the coins

hd = x//50
x %= 50

q = x//25
x %= 25

d = x//10
x %= 10

n = x//5

p = x% 5

print("half dollar:", hd, "\nquarter:", q, "\ndimes:", d, "\nnickels:", n, "\npennies:", p)
'''

'''
#Change in coins

amount=eval(input("Please enter some amount of money: "))
amount=int(amount*100)

hd=amount//50	# half dollars
amount%=50

q=amount//25	# quarters 
amount%=25

d=amount//10	# dimes
amount%=10

n=amount//5	# nickels
p=amount%5		# pennies

print("half dollars: ",hd,"quarters: ",q,"dimes: ",d,"nickels: ",n,"pennies: ",p, sep='\n')
'''

'''
#reverse 3d
x = int(input("number: "))
#print(x%10, (x//10)%10, x//100, sep ='')
y = (x%10)*100 + (x//10%10)*10 + x//100
print(y)
'''

'''
#print n even with while
n = int(input("number: "))

i = 2
while i <= n:
    print(i)
    i += 2
'''

#print star
x = int(input("number: "))

i = 1
while i <= x:
    print(i*'*')
    i += 1
