#one uppers
def one_upper(s):
    '''
    x = []
    x.extend(a)
    x.sort

    flag = False

    if x[0].isupper():
        flag = True

    if x[1].isupper():
        flag = False

    return flag
    '''
    count = 0
    
    for i in s:
        if i.isupper():
            count += 1

    if count == 1:
        return True
    else:
        return False

#clean
def clean(x):
    '''
    for i in range(len(x)):
        x[i] = splitter(x[i])

    return x
    '''
    return [splitter(i) for i in x]

def splitter(s):
    '''
    #string.puncuation
    a = s.replace(',','')
    a = a.replace('.','')
    a = a.replace(';','')
    return a
    '''

    exclude=',.;'
    a = ''
    for i in s:
        if i in exclude:
            continue
        else:
            a += i

    return a

##a = ['asd','er,', 'rt.', 'fgh;']
##print(clean(a))


#File I/O
f = open('bears.txt')

##for i in f: #for line in f
##    print(i)

z = f.read()
print(z)
