def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('Input some text: ')
something = something.replace(' ','')
something = something.replace(',','')
something = something.replace('.','')
something = something.replace('-','')

#all -> .?!:;-—()[]...’“”/,
#forbiden = ('.','?','!',':',';','-','—','(',')','[',']','.','.','.','’','“','”','/,)
#something = something.replace(forbiden, '')
#for i in bla bla bla

something = something.lower()
print(something)

if (is_palindrome(something)):
    print('Yeah it\'s palyndrom')
else:
    print('Not a palyndrom')

