class ShortInputException(Exception):
    '''user class for exceptions'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something: ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('EOFError')
except ShortInputException as ex:
    print('ShortInputException: length of entered string -- {0}; and minimal is {1}'.format(ex.length, ex.atleast))
else:
    print('No exceptions')