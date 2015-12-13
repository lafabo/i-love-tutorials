while True:
    s = input('Enter something(or "exit"): ')

    if s == 'exit':
        break
    if len(s) < 3:
        print('more than 3 chars, pls')
        continue                                #used to skip all others comands in block
    print('That\'s good len for string!')

