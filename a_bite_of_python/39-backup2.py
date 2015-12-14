import os
import time

source = '.'
target_dir = './backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
print('Dir created ',today)

target = today + os.sep + now + '.zip'
zip_command = 'zip -qr {0} {1} '.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup ', target, ' created')
else:
    print('Something wrong')