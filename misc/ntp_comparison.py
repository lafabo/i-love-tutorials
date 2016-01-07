'''
Totally useless utility to check is Network Time Protocol Servers shows the one time
I have no idea who may needs this, but why not?

for first script will parse
http://support.ntp.org/bin/view/Servers/StratumOneTimeServers
list and each "details" page to get host

for second it will save list in the file

and finally it will send requests with cycle to each time servers,
get "middle" variable and compare with result of requests,
and of course print it on the screen
'''

import ntplib
from time import ctime

