N = int(input())
M = int(input())
x = int(input())
y = int(input())

if N > M:
    q = [x,y, M-x, N-y]
else:
    q = [x, y, N-x, M-y]

j = []

for i in q:
    if i >= 0:
        j.append(i)

print(min(j))