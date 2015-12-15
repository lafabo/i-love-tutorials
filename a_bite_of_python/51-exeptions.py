try:
    text = input('Enter something: ')
except EOFError:
    print('EOFError')
except KeyboardInterrupt:
    print('Aborted by user')
else:
    print('You entered {0}'.format(text))