
#lambda
a = lambda x,y : x+y

#reverse string
def reverse_string(s):
    #return s[::-1]
    x = list(s)
    x.reverse()
    return ''.join(x)
