def printmax(a,b):
    if a > b:
        print(a, 'max')
    if a == b:
        print(a, '==', b)
    else:
        print(b, 'max')


printmax(3,6)
printmax(8,8)

a = int(input("A: "))
b = int(input("B: "))
printmax(a,b)

