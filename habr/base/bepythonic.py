# http://www.cafepy.com/article/be_pythonic/

#!/usr/bin/env python
#coding: utf8

'''
f = open('filename.csv') # f is an iterator
field_names = f.next().split(',') # get the first item from the iterator using next()
records = [dict(zip(field_names, line.split(','))) for line in f] # this will pull remaining lines
print sum(int(record['quantity']) for record in records)
'''


