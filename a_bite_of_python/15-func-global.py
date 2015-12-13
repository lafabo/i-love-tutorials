x = 50
def func():
    global x
    print('x = ',x)
    x = 2
    print('Changing x to ', x)

func()
print('Now x is ', x)