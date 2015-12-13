#!/usr/bin/env python3
import sys, os

print('Command line arguments:')
for i in sys.argv:
    print(i)

print('\n\nPYTHONPATH var consist', sys.path, '\n')


#if launch this with command line and add some arguments
#they will appear in sys.argv


print('Now let\'s see where is this programm is: ', os.getcwd())