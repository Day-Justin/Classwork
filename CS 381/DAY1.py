from turtle import*

'''
#hello world
name = input("what is your name? ")
print("hello", name)
'''

'''
#temp
temp = input("what temp in f ")
temp = int(temp)
temp = (temp - 32) * (5/9)
print(temp)
'''

'''
#generator
for i in range(5):
    print("Hello")
'''

'''
#t.square
for i in range(4):
    pendown()
    forward(100)
    right(90)
'''

'''
#t.reverseTriagnle
for i in range(3):
    pendown()
    forward(100)
    right(120)
'''    

'''
#t.triangle
for i in range(3):
    pendown()
    forward(100)
    left(120)
'''

'''
#t.hexagon
for i in range(6):
    pendown()
    forward(100)
    right(60)
'''

'''
#t.circle
for i in range(360):
    pendown()
    forward(1)
    right(1)
'''

'''
#t.pentagon
for i in range(5):
    pendown()
    forward(100)
    right(144)
'''

'''
#sum 2 inputs
first = eval(input("Please enter the first number: "))
second = int(input("Please enter the second number: "))
print("the sum of ", first, " and ", second, " is ", first + second)
'''


# The Python “sum” program
print("Welcome to the addition program.")
print("You can enter values for x and y and I will calculate ")
print("and display the sum.")
print() # prints a blank line
x=input("Please enter a value for x (entering 'done' terminates the program): ")
while x !='done': # this a ‘while loop’. It’s an example of “control”. 
    x=int(x)
    y=int(input("Please enter a value for y: "))
    sum=x+y
    print("The sum of ",x," and ",y," is: ",sum)
    print()
    x=input("Please enter a value for x (entering 'done' terminates the program): ")
print(
print("Thanks for trying our program!")
