
'''
#print args
print(1,2,3,sep='\n')
'''

'''
#walrus
#print(a=7)
print(a:=7)
'''

'''
#Rounding
x = eval(input("enter number"))
n = eval(inpput("enter precision"))
rounding1(x, n):
    round(x, n)

#rounding2(x, n):
'''

'''
#echo
n = int(input("please enter an integer: "))
#print("is", x, "even", not(bool(x%2)))
#print("is", x, "even", x%2 == 0)
print(n, "is", (n%2 == 0) * 'EVEN' + (n%2 != 0) * 'ODD')
'''


#Wage
h = eval(input('Please enter number of hours worked: '))
r = eval(input('Please enter your hourly rate:  '))
o = h - 40
#print("You earned $", (h*r) + ((h>40)*(o*r*.5)), " for ", h, " hours of work at $", r, "/hour", sep='')
print("You earned ", format(((h*r) + ((h>40)*(o*r*.5)), ',2f'), "for", format(h, ',2f'), "hours of work at", format(r, ',2f'), "/hour")
