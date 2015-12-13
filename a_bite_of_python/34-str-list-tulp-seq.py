shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'Boris'

#indexing operation
print('Element 0 ', shoplist[0])
print('Element 1 ', shoplist[1])
print('Element 2 ', shoplist[2])
print('Element 3 ', shoplist[3])
print('\nElement -1 ', shoplist[-1])
print('Element -2 ', shoplist[-2])
print('Zero element ', name[0])


#cutting from the list
print('Elements from 1 to 3 ', shoplist[1:3])
print('Elements from 2 to the end ', shoplist[2:])
print('Elements from 1 to -1', shoplist[1:-1])
print('Elements all ', shoplist[:])

#cutting from str
print('Symbols 1 - 3 ', name[1:3])
print('Symbols from 2 to the end ', name[2:])
print('Symbols 1 - -1 ', name[1:-1])
print('Symbols from begin to end: ',name[:])