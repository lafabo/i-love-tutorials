import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']
print(shoplist)

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)