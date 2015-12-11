from math import ceil
a = int(input())

a = map(int, str(a))
k = list(a)

if len(k)>1:
    print(k[len(k)-2])
else:
    print(0)