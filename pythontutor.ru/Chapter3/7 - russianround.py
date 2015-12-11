from math import ceil, floor
num = float(input())

def sovietround(num):
    if num>=0:
        if num-floor(num)>=0.5:
            return ceil(num)
        else:
            return floor(num)

print(sovietround(num))