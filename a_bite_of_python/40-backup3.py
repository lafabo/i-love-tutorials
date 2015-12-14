import os
import time

source = '.'
target_dir = './backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Enter the comment: ')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '__') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
print('Dir created ', today)

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup created ', target)
else:
    print('Something wrong')

