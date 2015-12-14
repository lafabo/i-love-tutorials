print('Simple "=" ')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]

print('shoplist: ', shoplist)
print('mylist: ', mylist)

print('Copy by full cut')
mylist = shoplist[:]
del mylist[0]

print('shoplist: ', shoplist)
print('mylist: ', mylist)

#always copy by the a = b[:]
#if just a = b then a[0] +1 => b[0]+1
#reference as is