def printmax(x,y):
    '''From 2 numbers

    return the biggest.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, ' bigger')
    else:
        print(y, ' bigger')

printmax(3,5)
print(printmax.__doc__)
print('the same as help(printmax) as i guess')