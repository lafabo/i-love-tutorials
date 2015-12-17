import os
import time
import argparse
import zipfile

#parsing comand line arguments
#-v for version
#-d for chouse dir
parser = argparse.ArgumentParser(description="Backup files in folder you choose\
                                in command line argument to that_folder/backup")
parser.add_argument('-v', help='version 0.0.9')
parser.add_argument('-d', help='place here the DIR you like to backup')
args = parser.parse_args()

#default setting (curent folder with script)
source = '.'
target_dir = 'backup'

if args.d != 0:
    source = args.d
else:
    target_dir = './'+target_dir

path = os.path.join(source, target_dir)
comment = input('Enter the comment: ')

if len(comment) == 0:
    name = time.strftime('%Y%m%d%H%M%S') + '.zip'
else:
    name = time.strftime('%Y%m%d%H%M%S') + '_' + comment.replace(' ', '__') + '.zip'

if not os.path.exists(path):
    os.mkdir(path)
print('Dir created ', path, target_dir)

def zipdir(source, name):
    for root, dirs, files in os.walk(path):
        for file in files:
            name.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile(name, 'w')
    zipdir(source, zipf)
    zipf.close()
    print('Backup created ',path,'/',name)
else:
    print('something wrong')