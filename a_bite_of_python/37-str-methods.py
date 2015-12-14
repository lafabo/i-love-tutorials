name = 'Boris'

if name.startswith('Bor'):
    print('Yeah, string starts with "Bor"')

if 'a' in name:
    print('"a" in name')

if name.find('ris') != -1:
    print('Yeah, string have "ris"')

delimiter = '_*_'

mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))

