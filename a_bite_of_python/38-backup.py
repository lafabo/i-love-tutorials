import os
import time

source = '.'

target_dir = './backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

print(zip_command)

if os.system(zip_command) == 0:
    print('BackUp done!')
else:
    print('Something wrong')

