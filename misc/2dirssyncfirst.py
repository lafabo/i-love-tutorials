#!/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
copy all files with ftp to DST, which are in SRC, and not in DST
'''

import urllib, os, filecmp, pysftp

server = '192.168.0.186'
port = '2121'
user = 'qwer'
pwd = '1234'


# filelist
def browsedirs(src, dst):
    # difference
    # !!!! works only in directories, not subdirectories
    download = [src + os.sep + x for x in filecmp.dircmp(src, dst).left_only]
    return download

# download and place it in dst/{filename}
with pysftp.Connection(server, username=user, password=pwd, port=port) as sftp:
    for file in download:
        sftp.cd(os.path.abspath())
        print ('ftp://qwer:1234@192.168.0.186:2121/%s' % file)
        urllib.urlretrieve(('ftp://qwer:1234@192.168.0.186:2121/%s' % file), (dst + os.sep + os.path.basename(file)))
