'''
This file completely doing nothing

all code here only to use some keywords, as Book requires
'''

#and
if 1==1 and 2 != 0:
	print "AND"

text = 'Always look at the bright side of Sun'
print text

del text
print "text DELeted"

from math import e
print e , " that was FROM"

if not 0 == 1:
	print "NOT text"

i = 0
while i < 3:
	print("WHILE")
	i += 1
#import
import random as rnd

print rnd.randint, "AS"

if i != 0:
	print "!=0"
elif i == 0:
	print "ELIF"
else:
	print 'ELSE'

def dd():
	global z
	z = "GLOBAL"

dd()
print z

print (1 != 0 or 2 != 1)

with open('with.txt') as fd:
	print "WITH"

#ASSET, pass
def dunno():
	b = 2
	assert (b > 1)
	pass

while True:
	print "BREAK"
	break

try:
	k = 1 / 0
except ZeroDivisionError:
	k = 0
	print "EXCEPT"


#CLASS
class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print "Dog ", self.name, self.age

bob=Dog("Bob", "6")

#EXEC
text = "print 'EXEC'"
exec text

#RAISE
try:
	raise NameError, "RAISE ERROR"
except NameError:
	print "RAISE ERROR MISSED TARGED"

#continue
for i in "hello world":
	if i == "o":
		continue
	print i*2,

try:
	k = 1 / 0
except ArithmeticError:
	k = 0
finally:
	print '\n', k+1

#IS
a = 100
b = 100

print "a = ", a, " b = ", b
if a == b:
	print "a == b True"
else:
	print "a != b False"

if a is b:
	print "a is b"
else:
	print "a isn't b"

list = map(lambda x: x*2, [1, 2, 3, 4])
print list

poem = '''
\t \\The Whale\\ \a\a\a
The whale sailed \vslow beneath the moon,\nIts baby by its side,
Crossing\r oceans three miles deep
And thousands \fof cold miles wide.

\tThat\'s all!\b'''
#\a - system bell
#\b - backspace

print poem


'''formating
d	Signed integer decimal.
i	Signed integer decimal.
o	Unsigned octal.
u	Unsigned decimal.
x	Unsigned hexadecimal (lowercase).
X	Unsigned hexadecimal (uppercase).
e	Floating point exponential format (lowercase).
E	Floating point exponential format (uppercase).
f	Floating point decimal format.
F	Floating point decimal format.
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c	Single character (accepts integer or single character string).
r	String (converts any python object using repr()).
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result.'''
#print "There is \%d - %d for int, and \%i for"

#todo Yeild