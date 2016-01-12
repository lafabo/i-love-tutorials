
def do_twice(f, s):
    f(s)
    f(s)

def print_twice(s):
    print s
    print s

do_twice(print_twice, 'spam')
print ''

def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)

do_four(print_twice, 'sram')
print ''
