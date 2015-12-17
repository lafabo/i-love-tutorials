import os, zipfile, argparse, time

def backup(path, name, compression):
    '''BackUp dir to zip

    zip created in subdir /backup
    you can chose dir and compression/storing (storing by default)
    '''


    list = os.listdir(path)
    print(list)
    file = zipfile.ZipFile(name,'w', compression)
    print(file)
    for item in list:
        file.write(item)
        print(item)
    file.close()

parser = argparse.ArgumentParser(description="Backup files in folder you choose\
                                in command line argument to that_folder/backup")
parser.add_argument('-v', help='version 0.0.9')
parser.add_argument('-d', help='place here the DIR you like to backup')
parser.add_argument('-c', help='use this key to store with compression')
args = parser.parse_args()

print(args.d, args.c)

comment = input('Comment: ')
arguments = {}
if comment !='':
    arguments['name'] = time.strftime('%Y%m%d%H%M%S') + '_' + comment.replace(' ', '__') + '.zip'
else:
    arguments['name'] = time.strftime('%Y%m%d%H%M%S') + '.zip'
if args.d:
    arguments['path'] = args.d
    path = args.d
else:
    arguments['path'] = '.'
    path = '.'

if args.c:
    arguments['compression'] = zipfile.ZIP_DEFLATED
else:
    arguments['compression'] = zipfile.ZIP_STORED

print(arguments)

if not os.path.exists(path+os.sep+'backup'):
    os.mkdir(path+os.sep+'backup')
print('Dir created ', path+os.sep+'backup')


backup(path=arguments['path'], name=arguments['name'], compression=arguments['compression'])
del arguments