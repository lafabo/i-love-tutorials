'''
I want a quick pnone number detector
only for russia and urkaine

run from the bash in format whatthephone.py +xxxxxxxxxxxxx international format only

It will can:
1. get short numbers in format whatthephone.py xxxx mobileoperator
2. get country / mobile operator
3. look in a few phone number sites for a quick users replays about it
'''

import sys

num = ''
try:
    num = sys.argv[1]
except:
    print 'Wrong number'

#           always XX in the end
ua_list = ['http://ktozvonit.com.ua/nomer/06600231XX', 'http://zvonki.octo.net/number.aspx/9281134858']
ru_list = ['http://zvonki.octo.net/number.aspx/8926']


if num[:2] == '+38':
    numtype = 'ua'
elif num[:2] == '+7':
    numtype = 'ru'
elif num[0] != '+' and len(num) <= 4:
    numtype = 'short'
else:
    print 'bad number'
    exit(1)

def checkoperator(num):
#mobileoperator:
    uanum = {'039': 'Kievstar (Golden Telecom)',
             '050': 'MTS',
             '063': 'Life:)',
             '066': 'MTS',
             '067': 'Kievstar',
             '068': 'Kievstar',
             '091': 'Utel',
             '092': 'PeopleNet',
             '093': 'Life:)',
             '094': 'Intertelecom',
             '095': 'MTS',
             '096': 'Kievstar',
             '097': 'Kievstar',
             '098': 'Kievstar',
             '099': 'MTS',
             '800': 'Free to call number',
             '900': 'Number with additional payment'
             }

    # no Tele2 codes and additional info like operators 'daughters' and regions todo add it!
    runum = {'910': 'MTS',
             '911': 'MTS',
             '912': 'MTS',
             '913': 'MTS',
             '914': 'MTS',
             '915': 'MTS',
             '916': 'MTS',
             '917': 'MTS',
             '918': 'MTS',
             '919': 'MTS',
             '980': 'MTS',
             '981': 'MTS',
             '982': 'MTS',
             '983': 'MTS',
             '984': 'MTS',
             '985': 'MTS',
             '986': 'MTS',
             '987': 'MTS',
             '988': 'MTS',
             '989': 'MTS',
             '903': 'Beeline',
             '905': 'Beeline',
             '906': 'Beeline',
             '909': 'Beeline',
             '960': 'Beeline',
             '961': 'Beeline',
             '962': 'Beeline',
             '963': 'Beeline',
             '964': 'Beeline',
             '965': 'Beeline',
             '966': 'Beeline',
             '967': 'Beeline',
             '968': 'Beeline',
             '976': 'Beeline',
             '920': 'Megafon',
             '921': 'Megafon',
             '922': 'Megafon',
             '923': 'Megafon',
             '924': 'Megafon',
             '925': 'Megafon',
             '926': 'Megafon',
             '927': 'Megafon',
             '928': 'Megafon',
             '929': 'Megafon',
             '930': 'Megafon',
             '931': 'Megafon',
             '932': 'Megafon',
             '933': 'Megafon',
             '934': 'Megafon',
             '935': 'Megafon',
             '936': 'Megafon',
             '937': 'Megafon',
    }


