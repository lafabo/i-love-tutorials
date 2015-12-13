def func_outer():
    x = 2
    y = 3
    z = 4
    print('x =', x)
    print('y =', y)
    print('z =', z)

    def func_inner():
        nonlocal x
        global y
        x = 5
        y = 6
        z = 7

    func_inner()

    print('Local x changed to ', x)
    print('Local y changed to ', y)
    print('Local z changed to ', z)

func_outer()