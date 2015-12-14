bri = set(['Brazil', 'Russia', 'India'])
if 'India' in bri:
    print('True')

if 'USA' in bri:
    print('True')
else:
    print('False')

bric = bri.copy()
bric.add('China')
if bric.issuperset(bri):
    print('bric is superset bri')
else:
    print('bric isn\'t superset bri')

bri.remove('Russia')

print(bri & bric) #OR bri.intersection(bric)
print(bri.intersection(bric))