from math import *

n = int(input('Enter the rage: -'))
p = [2, 3]
count = 2
a = 5
while count < n:
    b = 0
    for i in range(2, a):
        if i <= sqrt(a):
            if a % i == 0:
                print(a, ' is a complex number')
                b = 1
            else:
                pass
    if b != 1:
        print(a, ' is a prime number')
        p = p + [a]
    count += 1
    a += 2

print(p)

'''this program i copied in A Bite... And as i see
it's don't work properly... I think i just pass it
and start the next example'''