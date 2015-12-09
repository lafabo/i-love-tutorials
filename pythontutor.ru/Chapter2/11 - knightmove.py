a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(c - a) == abs(d - b) or (a == c) or (b == d):
    print("YES")
else:
    print("NO")
    