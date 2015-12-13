shoplist = ['apples', 'mango', 'carrot', 'banana']

print('I need to buy ', len(shoplist), 'items')

print('Shop list:', end = ' ')
for i in shoplist:
    print(i, end=' ')

print('\n\nalso i shoud buy rice')
shoplist.append('rice')
print('Now my shoplist looks like this: ', shoplist)

print('sort the shoplist ')
shoplist.sort()
print('sorted shop list looks like: ', shoplist)

print('the firs i should to buy: ', shoplist[0])

olditem = shoplist[0]
del shoplist[0]

print('I bought ', olditem)
print('What\'s next? ', shoplist)