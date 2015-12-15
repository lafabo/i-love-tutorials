i = []
i.append('item')

print(repr(i))
print(eval(repr(i)))
print(eval(repr(i))==i)