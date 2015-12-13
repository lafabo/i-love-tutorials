x = 50
def func(x):
    print('x = ', x)
    x = 2
    print('changing local x to ', x)

func(x)
print('x still = ', x)