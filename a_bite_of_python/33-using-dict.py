book = {'mike'  : 'good guy',
        'sam'   : 'bad guy',
        'michel': 'om nom nom',
        'jack'  : 'a traitor',
        }

print('Mike: ', book['mike'])

del book['jack']
print('\n Now, without Jack here is {0} contacts'.format(len(book)))

for nm, des in book.items():                            
    print('\n {0} is a {1}'.format(nm, des))

book['jimbo']='dump'

if 'jimbo' in book:
    print('\n Jimbo: ', book['jimbo'])
